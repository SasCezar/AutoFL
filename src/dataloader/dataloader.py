from abc import ABC, abstractmethod
from pathlib import Path


class DataLoaderBase(ABC):
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    @abstractmethod
    def load(self):
        pass