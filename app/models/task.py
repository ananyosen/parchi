from dataclasses import dataclass

@dataclass
class Task:
    id: int = None
    uuid: str = ""
    metadata: str = ""
    type: str = ""
    status: str = "CREATED"
    description: str = ""