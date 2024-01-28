from typing import List, Union, Tuple

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class CascadeEnsemble(EnsembleBase):
    """
    Ensemble method that iterates over the annotations and picks the first annotation that is not unannotated.
    """
    def run(self, annotations: List[Annotation]) -> Tuple[Union[List | np.array], int]:
        for annotation in annotations:
            if not annotation.unannotated:
                return annotation, 0

        return annotations[0], 1
