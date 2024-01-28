from typing import List, Tuple, Union

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class NoneEnsemble(EnsembleBase):
    """
    Ensemble method that does not do anything. This is useful for single annotator experiments.
    """

    def run(self, annotations: List[Annotation]) -> Tuple[Union[List | np.array], int]:
        return annotations[0], 0
