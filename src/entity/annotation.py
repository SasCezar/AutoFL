from typing import List

from pydantic import BaseModel


class Annotation(BaseModel):
    distribution: List[float]
    labels: List[str]
    filtered: bool
