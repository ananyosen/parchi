from ..repositories.primary import tasks_repo as task_repo
from ..models.task import Task

async def get_all_tasks() -> list[Task]:
    """
    Retrieve all tasks.
    """
    return task_repo.get_all_tasks()

async def get_task_summary() -> dict:
    """
    Retrieve a summary of all tasks.
    """
    tasks = task_repo.get_all_tasks()
    summary = {
        "total_tasks": len(tasks),
        "tasks_by_type": {}
    }
    
    for task in tasks:
        if task.type not in summary["tasks_by_type"]:
            summary["tasks_by_type"][task.type] = {}
            summary["tasks_by_type"][task.type][task.status] = 1
        elif task.status not in summary["tasks_by_type"][task.type]:
            summary["tasks_by_type"][task.type][task.status] = 1
        else:
            summary["tasks_by_type"][task.type][task.status] += 1
    
    return summary