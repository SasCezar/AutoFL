from abc import ABC

from entity.project import File
from entity.taxonomy import TaxonomyBase


class LFBase(ABC):
    def __init__(self, taxonomy: TaxonomyBase):
        self.taxonomy = taxonomy

    def label(self, file: File):
        pass