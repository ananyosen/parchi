from fastapi import FastAPI

from .routers import docs

from .utils import env

app = FastAPI()

app.include_router(docs.router)

@app.get("/health-check")
def health_check():
    return {"status": "healthy"}

env.validate_env_variables()