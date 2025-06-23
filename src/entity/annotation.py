from typing import List

from pydantic import BaseModel


class Annotation(BaseModel):
    """
    Class defining the annotation assigned to a file.
    """

    distribution: List[float]
    unannotated: int
    raw_annotation: List[float] = None
