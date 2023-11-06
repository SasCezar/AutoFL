
from typing import List, Union

import numpy as np

from ensemble.ensemble import EnsembleBase


class AverageEnsemble(EnsembleBase):
    """
    Ensemble method that averages the annotations.
    """
    def run(self, annotations: List[Union[np.array, List]]):
        mean = np.mean(annotations, axis=0)
        return mean
