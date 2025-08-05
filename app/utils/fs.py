import os

def check_or_create_directory(dir_path):
    """Check if a directory exists, and create it if it doesn't."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)