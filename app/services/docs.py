import os
from fastapi import UploadFile
from fastapi.responses import FileResponse
import uuid
import json

from ..utils import env, fs
from ..utils import file as file_utils

from ..repositories.primary import tasks as task_repo
from ..repositories.primary import assets as asset_repo

from ..repositories.vector import ml as ml_repo

from ..models.task import Task
from ..models.asset import Asset

async def save_file(file: UploadFile):
    """
    Save the uploaded file to a specific location.
    """
    config = env.get_config()
    asset_dir = os.path.join(config['asset_store_path'], 'assets')
    fs.check_or_create_directory(asset_dir)
    unique_id = uuid.uuid4()
    file_location = os.path.join(asset_dir, f"{unique_id}_{file.filename}")
    with open(file_location, "wb") as f:
        content = await file.read()
        content_hash = file_utils.generate_hash(content)
        is_duplicate = asset_repo.check_is_duplicate_asset(content_hash)
        if is_duplicate:
            return {"error": "file already exists", "status": "duplicate"}
        f.write(content)

    content_type = file.content_type or "application/octet-stream"
    asset = Asset(
        uuid=str(unique_id),
        filename=file.filename,
        metadata=json.dumps({"content_type": content_type}),
        path=file_location,
        content_type=content_type,
        content_hash=file_utils.generate_hash(content),
        status="CREATED"
    )
    asset_repo.save_asset(asset)

    task = Task(
        type="extract",
        metadata=json.dumps({"filename": file.filename, "location": file_location, "file_id": str(unique_id)}),
        description="Document processing task",
        status="CREATED",
        uuid=str(uuid.uuid4())
    )
    task_repo.queue_task(task)
    return {"filename": file.filename, "location": file_location, "status": "queued"}

async def get_all_documents():
    """
    Retrieve all documents from the asset repository.
    """
    assets = asset_repo.get_all_assets()
    return assets

async def search_documents(query: str) -> list:
    """
    Search documents in the vector database.
    """
    if not query:
        return []

    results = ml_repo.query_vector_db(query)
    return results

async def debug_search_documents(query: str) -> dict:
    """
    Debug search documents in the vector database.
    """
    results = await search_documents(query)
    if not results:
        return {"error": "No documents found"}
    
    first_result = results[0]
    asset = asset_repo.get_asset_by_id(first_result.metadata.get("file_id"))
    
    if not asset:
        return {"error": "Asset not found"}
    
    return FileResponse(
        asset.path,
        media_type=asset.content_type,
        filename=asset.filename,
        headers={"Content-Disposition": f"inline; filename={asset.filename}"}
    )