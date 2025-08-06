from fastapi import APIRouter, UploadFile

from ..services import tasks as tasks_service

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
