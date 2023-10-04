from typing import Optional, List

from pydantic import BaseModel

from entity.annotation import Annotation


class File(BaseModel):
    """
    Class defining a file. Each file has a path, a language, a content, a list of identifiers and a package.
    """
    path: str
    language: str
    content: Optional[str] = None
    identifiers: Optional[List[str]] = None
    package: Optional[str] = None
    annotation: Optional[Annotation] = None
