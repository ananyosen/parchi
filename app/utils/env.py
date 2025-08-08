import os
from ..constants import env as env_constants

def validate_env_variables():
    """Check if required environment variables are set."""
    if not os.getenv(env_constants.ASSET_STORE_PATH):
        raise EnvironmentError(f"{env_constants.ASSET_STORE_PATH} environment variable is not set.")
    
    if not os.getenv(env_constants.PERSIST_PATH):
        raise EnvironmentError(f"{env_constants.PERSIST_PATH} environment variable is not set.")
    
def get_config():
    """Load configuration from environment variables."""
    return {
        "asset_store_path": os.getenv(env_constants.ASSET_STORE_PATH),
        "persist_path": os.getenv(env_constants.PERSIST_PATH)
    }