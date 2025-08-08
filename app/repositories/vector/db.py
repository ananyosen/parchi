from contextlib import contextmanager

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from ...constants.types import CHROMA_COLLECTION_NAME

from ...utils.fs import get_model_path, get_vector_db_path

@contextmanager
def vector_db_session():
    """Context manager for vector database sessions."""
    try:
        embedding = HuggingFaceEmbeddings(model_name=get_model_path())
        vectordb = Chroma(
            collection_name=CHROMA_COLLECTION_NAME,
            embedding_function=embedding,
            persist_directory=get_vector_db_path()
        )
        print(f"debug paths {get_model_path()} {get_vector_db_path}")
        yield vectordb
    except Exception as e:
        print(f"Error occurred in vector DB session: {e}")
    finally:
        pass