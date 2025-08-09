from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

from ..services import assets_service

router = APIRouter(
    prefix="/assets",
    tags=["Files"],
)

@router.post("/upload")
async def upload_files(files: list[UploadFile]):
    """
    Upload a file and return its filename.
    """
    return [await assets_service.save_file(file) for file in files]

@router.get("/")
async def get_docs():
    """
    Retrieve all documents.
    """
    return await assets_service.get_all_documents()

@router.get("/search")
async def search_docs(query: str):
    """
    Search documents in the vector database.
    """
    return await assets_service.search_documents(query)

@router.get("/debug/search")
async def debug_search_docs(query: str):
    """
    Debug search documents in the vector database.
    """
    return await assets_service.debug_search_documents(query)
