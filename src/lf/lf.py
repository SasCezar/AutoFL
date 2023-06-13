from abc import ABC

import numpy as np

from entity.taxonomy import TaxonomyBase


class LFBase(ABC):
    def __init__(self, taxonomy: TaxonomyBase):
        self.taxonomy = taxonomy
        self.content = True

    def annotate(self, name, content) -> np.array:
        pass