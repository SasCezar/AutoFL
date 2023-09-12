from typing import List, Dict, Optional

from pydantic import BaseModel


class Analysis(BaseModel):
    """
    Class modelling the analysis run. Contains the project info and configs for the annotation.
    """
    name: str
    remote: str
    languages: List[str]
    config: Optional[Dict[str, str]] = None
