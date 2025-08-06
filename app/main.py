from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.repositories.primary.db import initialize_db

from .routers import docs, tasks

from .utils import env
from .repositories.primary.db import initialize_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(docs.router)
app.include_router(tasks.router)


@app.get("/health-check")
def health_check():
    return {"status": "healthy"}

env.validate_env_variables()