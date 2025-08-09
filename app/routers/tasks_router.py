from fastapi import APIRouter, UploadFile

from ..services import tasks_service as tasks_service

router = APIRouter(
    prefix="/tasks",
    tags=["Files"],
)

@router.get("/")
async def get_all_tasks():
    """
    Retrieve all tasks.
    """
    return await tasks_service.get_all_tasks()

@router.get("/summary")
async def get_task_summary():
    """
    Retrieve a summary of all tasks.
    """
    return await tasks_service.get_task_summary()