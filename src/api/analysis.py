from typing import List

from pydantic import BaseModel

from entity.project import Project


class Analysis(BaseModel):
    project: Project
    name: str
    remote: str
    languages: List[str]
