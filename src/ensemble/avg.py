
from typing import List, Union

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class AverageEnsemble(EnsembleBase):
    """
    Ensemble method that averages the annotations.
    """
    def run(self, annotations: List[Annotation]):
        annotations = [x.distribution for x in annotations if not x.unannotated]
        mean = np.mean(annotations, axis=0)
        return mean
