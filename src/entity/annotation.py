from pathlib import Path
from typing import List

from pydantic import BaseModel


class Annotation(BaseModel):
    file: Path
    distribution: List[float]
    labels: List[str]
    unannotated: bool
