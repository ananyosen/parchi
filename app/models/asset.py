from dataclasses import dataclass

@dataclass
class Asset:
    id: int = None
    uuid: str = None
    filename: str = None
    metadata: str = None
    path: str = None
    content_type: str = None
    content_hash: str = None
    status: str = None