import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.gzip import GZipMiddleware

from apscheduler.schedulers.background import BackgroundScheduler
from .constants.env import FRONTEND_BUILD_DIR, FRONTEND_ASSETS_DIR

from .repositories.primary.db import initialize_db

from .routers import docs, tasks

from .utils import env
from .utils.cached_static_file import CacheControlledStaticFiles
from .jobs import jobs as scheduler_jobs

scheduler = BackgroundScheduler()
scheduler.add_job(scheduler_jobs.start_task_processing, "interval", minutes=10)

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    scheduler.start()
    yield
    scheduler.shutdown(wait=False)

app = FastAPI(lifespan=lifespan)
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(docs.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")

@app.get("/api/health-check")
def health_check():
    return {"status": "healthy"}


# frontend file server
app.mount(f"/{FRONTEND_ASSETS_DIR}", CacheControlledStaticFiles(directory=os.path.join(FRONTEND_BUILD_DIR, FRONTEND_ASSETS_DIR)), name=FRONTEND_ASSETS_DIR)

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_BUILD_DIR, "index.html"))

@app.get("/{full_path}")
async def serve_react_app(full_path: str):
    return FileResponse(os.path.join(FRONTEND_BUILD_DIR, "index.html"))

env.validate_env_variables()