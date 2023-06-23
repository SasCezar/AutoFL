from abc import ABC
from pathlib import Path


class LoaderBase(ABC):
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def load(self):
        pass