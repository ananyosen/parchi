import PIL
import pytesseract
import json
import uuid

from ..models.task import Task
from ..repositories.primary import tasks as task_repo
from ..repositories.primary import assets as asset_repo
from ..constants.types import IMAGE_CONTENT_TYPES

def extract_text_from_asset(extract_task: Task) -> str:
    """Extract text from an image associated with a task.
    Args:
        task (Task): The task containing the image to process.
    Returns:
        str: The extracted text from the image.
    """
    try:
        extract_task.status = "PROCESSING"
        task_repo.update_task_status(extract_task.uuid, extract_task.status)
        asset_id = json.loads(extract_task.metadata).get("file_id")
        asset = asset_repo.get_asset_by_id(asset_id)
        if asset is None:
            extract_task.status = "FAILED"
            task_repo.update_task_status(extract_task.uuid, extract_task.status)
            return "Asset not found"
        
        asset_path = asset.path
        asset_type = asset.content_type
        if asset_type not in IMAGE_CONTENT_TYPES:
            extract_task.status = "FAILED"
            task_repo.update_task_status(extract_task.uuid, extract_task.status)
            return "Unsupported image type"
        with PIL.Image.open(asset_path) as img:
            text = pytesseract.image_to_string(img)
            extract_task.status = "COMPLETED"
            task_repo.update_task_status(extract_task.uuid, extract_task.status)
            print(f"task complete for asset id {asset_id}")
           
            index_task = Task(
                type="index",
                status="CREATED",
                metadata=json.dumps({
                    "file_id": asset_id,
                    "extracted_text": text
                }),
                description=f"Indexing text extracted from {asset.filename}",
                uuid=str(uuid.uuid4())
            )
            task_repo.queue_task(index_task)

            return "Text extracted successfully"
    except Exception as e:
        return f"Error extracting text: {e}"