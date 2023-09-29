from typing import List, Union

import numpy as np

from ensemble.ensemble import EnsembleBase


class CascadeEnsemble(EnsembleBase):
    """
    Ensemble method that iterates over the annotations and picks the first annotation that is not unannotated.
    """
    def run(self, annotations: List[Union[np.array, List]]):
        for annotation in annotations:
            if not annotation.unannotated:
                return annotation
        return annotations[0]
