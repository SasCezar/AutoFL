from abc import ABC

from entity.project import File
from entity.taxonomy import Taxonomy


class LF(ABC):
    def __int__(self, taxonomy: Taxonomy):
        self.taxonomy = taxonomy

    def label(self, file: File):
        pass