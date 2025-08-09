import hashlib

def generate_hash(content: bytes) -> str:
    """Generate a SHA-256 hash for the given file content."""
    return hashlib.sha256(content).hexdigest()