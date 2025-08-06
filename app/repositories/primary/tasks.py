from .db import db_session

from ...models.task import Task
def queue_task(task: Task):
    """Queue a task for processing."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (uuid, type, status, metadata, description) VALUES (?, ?, ?, ?, ?)",
            (task.uuid, task.type, task.status, task.metadata, task.description)
        )

def get_tasks_by_status(status: str) -> list[Task]:
    """Retrieve tasks by their status."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        )
        return [Task(**row) for row in cursor.fetchall()]

def get_task_by_type(type: str) -> list[Task]:
    """Retrieve tasks by their type."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE type = ?",
            (type,)
        )
        return [Task(**row) for row in cursor.fetchall()]

def get_task_by_id(task_id: str) -> Task | None:
    """Retrieve a specific task by its ID."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE uuid = ?",
            (task_id)
        )
        result = cursor.fetchone()
        if result:
            return Task(**result)
        return None

def update_task_status(task_id: str, status: str) -> None:
    """Update the status of a specific task."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE uuid = ?",
            (status, task_id)
        )

def get_all_tasks(page: int = 0, page_size: int = 100) -> list[Task]:
    """Retrieve all tasks."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks LIMIT ? OFFSET ?", (page_size, page * page_size))
        return [Task(**row) for row in cursor.fetchall()]