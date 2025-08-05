import os

def validate_env_variables():
    """Check if required environment variables are set."""
    if not os.getenv('ASSET_STORE_PATH'):
        raise EnvironmentError("ASSET_STORE_PATH environment variable is not set.")
    
def get_config():
    """Load configuration from environment variables."""
    return {
        "asset_store_path": os.getenv('ASSET_STORE_PATH'),
    }