import os
from fastapi import UploadFile
import uuid

from ..utils import env, fs
from ..tasks import docs as docs_tasks

async def save_file(file: UploadFile):
    """
    Save the uploaded file to a specific location.
    """
    config = env.get_config()
    asset_dir = os.path.join(config['asset_store_path'], 'assets')
    fs.check_or_create_directory(asset_dir)
    file_location = os.path.join(asset_dir, f"{uuid.uuid4()}_{file.filename}")
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"filename": file.filename, "location": docs_tasks.extract_text_from_image(file_location)}