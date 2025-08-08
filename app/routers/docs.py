from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

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

@router.get("/search")
async def search_docs(query: str):
    """
    Search documents in the vector database.
    """
    return await docs.search_documents(query)

@router.get("/debug/search")
async def debug_search_docs(query: str):
    """
    Debug search documents in the vector database.
    """
    return await docs.debug_search_documents(query)
