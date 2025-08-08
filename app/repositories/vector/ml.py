from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from .db import vector_db_session

def index_text(text: str, metadata: dict) -> None:
    """Index text into the vector database.
    
    Args:
        text (str): The text to index.
        metadata (dict): Metadata associated with the text.
    """
    with vector_db_session() as vectordb:
        doc = Document(page_content=text, metadata=metadata)
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents([doc])
        vectordb.add_documents(chunks)

def query_vector_db(query: str, top_k: int = 3) -> list:
    """Query the vector database.

    Args:
        query (str): The query string.
        top_k (int): The number of top results to return.

    Returns:
        list: A list of documents matching the query.
    """
    with vector_db_session() as vectordb:
        results = vectordb.similarity_search(query, k=top_k)
        return results