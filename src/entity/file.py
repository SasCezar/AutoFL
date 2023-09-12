from pathlib import Path
from typing import Optional, List

from pydantic import BaseModel


class File(BaseModel):
    """
    Class defining a source code file.
    """
    path: Path
    language: str
    content: Optional[str] = None
    identifiers: Optional[List[str]] = None
    package: Optional[str] = None
