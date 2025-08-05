from fastapi import APIRouter, UploadFile

from ..services import docs

router = APIRouter(
    prefix="/docs",
    tags=["Files"],
)

@router.post("/upload")
async def upload_files(file: UploadFile):
    """
    Upload a file and return its filename.
    """
    return await docs.save_file(file)
