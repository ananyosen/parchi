from dataclasses import dataclass

@dataclass
class Task:
    id: str = ""
    uuid: str = ""
    metadata: str = ""
    type: str = ""
    status: str = "CREATED"
    description: str = ""