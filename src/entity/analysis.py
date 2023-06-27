from typing import List, Dict, Optional

from pydantic import BaseModel


class Analysis(BaseModel):
    name: str
    remote: str
    languages: List[str]
    config: Optional[Dict[str, str]]
