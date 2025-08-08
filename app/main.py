from contextlib import asynccontextmanager
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

from .repositories.primary.db import initialize_db

from .routers import docs, tasks

from .utils import env
from .jobs import jobs as scheduler_jobs

scheduler = BackgroundScheduler()
scheduler.add_job(scheduler_jobs.start_task_processing, "interval", seconds=10)

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    scheduler.start()
    yield
    scheduler.shutdown(wait=False)

app = FastAPI(lifespan=lifespan)

app.include_router(docs.router)
app.include_router(tasks.router)


@app.get("/health-check")
def health_check():
    return {"status": "healthy"}

env.validate_env_variables()