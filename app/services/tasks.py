from ..repositories.primary import tasks as task_repo
from ..models.task import Task

async def get_all_tasks() -> list[Task]:
    """
    Retrieve all tasks.
    """
    return task_repo.get_all_tasks()