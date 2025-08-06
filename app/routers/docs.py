from fastapi import APIRouter, UploadFile

from ..services import docs

router = APIRouter(
    prefix="/assets",
    tags=["Files"],
)

@router.post("/upload")
async def upload_files(file: UploadFile):
    """
    Upload a file and return its filename.
    """
    return await docs.save_file(file)

@router.get("/")
async def get_docs():
    """
    Retrieve all documents.
    """
    return await docs.get_all_documents()