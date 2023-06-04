from typing import List

from pydantic import BaseModel


class Analysis(BaseModel):
    name: str
    remote: str
    languages: List[str]
