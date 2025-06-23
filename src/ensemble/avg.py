from typing import List

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class AverageEnsemble(EnsembleBase):
    """
    Ensemble method that averages the annotations.
    """

    def run(self, annotations: List[Annotation]) -> Annotation:
        annotated = np.array([x.distribution for x in annotations if not x.unannotated])
        if annotated:
            mean = np.mean(annotated, axis=0)
            return Annotation(distribution=mean.tolist(), unannotated=0)

        return Annotation(distribution=annotations[0].distribution, unannotated=1)
