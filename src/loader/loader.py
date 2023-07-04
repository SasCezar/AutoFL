from abc import ABC, abstractmethod
from pathlib import Path


class LoaderBase(ABC):
    def __init__(self, path: str | Path):
        self.path = Path(path)

    @abstractmethod
    def load(self):
        pass