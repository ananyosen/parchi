import threading
import time

from ..repositories.primary import tasks as task_repo
from ..tasks.ml import extract_text_from_asset

job_lock = threading.Lock()

def start_task_processing():
    """
    Start the task processing in a separate thread.
    """
    if not job_lock.acquire(blocking=False):
        print("Task processing is already running.")
        return

    try:
        created_tasks = task_repo.get_tasks_by_status("CREATED")
        print("tasks pending " + str(len(created_tasks)))
        for task in created_tasks:
            if task.type == "extract":
                print(f"Processing task {task.uuid} of type {task.type}")
                result = extract_text_from_asset(task)
                print(f"Task {task.uuid} processed with result: {result}")
            else:
                print(f"Skipping unsupported task type: {task.type}")

    finally:
        print("Task processing completed.")
        job_lock.release()