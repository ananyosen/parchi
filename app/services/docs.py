import os
from fastapi import UploadFile
import uuid
import json

from ..utils import env, fs
from ..repositories.primary.tasks import queue_task
from ..models.task import Task

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
        f.write(content)

    task = Task(
        type="document",
        metadata=json.dumps({"filename": file.filename, "location": file_location, "file_id": str(unique_id)}),
        description="Document processing task",
        status="CREATED",
        uuid=str(uuid.uuid4())
    )
    queue_task(task)
    return {"filename": file.filename, "location": file_location, "status": "queued"}