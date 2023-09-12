from pathlib import Path
from typing import Optional, List

from pydantic import BaseModel


class File(BaseModel):
    """
    Class defining a source code file.
    """
    path: Path
    language: str
    content: Optional[str]
    identifiers: Optional[List[str]]
    package: Optional[str]
