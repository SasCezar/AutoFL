from pathlib import Path
from typing import Optional, List

from pydantic import BaseModel


class File(BaseModel):
    path: Path
    language: str
    content: Optional[str]
    identifiers: Optional[List[str]]
