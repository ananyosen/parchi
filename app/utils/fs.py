import os
from .env import get_config
from ..constants import env as env_constants

def check_or_create_directory(dir_path):
    """Check if a directory exists, and create it if it doesn't."""
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except Exception as e:
            raise RuntimeError(f"Error creating directory {dir_path}: {e}")

def get_persist_path():
    """Get the path for persistent storage."""
    persist_path = get_config().get('persist_path')
    if not persist_path:
        raise EnvironmentError("PERSIST_PATH environment variable is not set.")
    check_or_create_directory(persist_path)
    return persist_path

def get_primary_db_path():
    """Get the path for the primary database."""
    db_path = os.path.join(get_persist_path(), 'primary.db')
    return db_path

def get_vector_db_path():
    """Get the path for the vector database."""
    vector_db_path = os.path.join(get_persist_path(), 'vector/')
    return vector_db_path

def get_model_path():
    """Get the path for a specific model."""
    model_path = os.path.join('.', 'models')
    check_or_create_directory(model_path)
    return model_path