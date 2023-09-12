from typing import List, Union

import numpy as np

from annotation import LFBase
from ensemble.ensemble import EnsembleBase


class Annotator:
    def __init__(self, lfs: List[LFBase], ensemble: Union[EnsembleBase, callable]):
        self.lfs = lfs
        self.ensemble = ensemble

    def annotate(self, name: str, content: str) -> np.array:
        labels = []
        for lf in self.lfs:
            labels.append(lf.annotate(name, content))

        node_labels = self.ensemble(labels)

        return node_labels
