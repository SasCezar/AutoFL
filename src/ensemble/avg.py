
from typing import List, Union, Tuple

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class AverageEnsemble(EnsembleBase):
    """
    Ensemble method that averages the annotations.
    """
    def run(self, annotations: List[Annotation]) -> Tuple[Union[List | np.array], int]:
        annotated = np.array([x.distribution for x in annotations if not x.unannotated])
        if annotated:
            mean = np.mean(annotated, axis=0)
            return mean, 0

        return annotations[0], 1
