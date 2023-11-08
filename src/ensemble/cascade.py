from typing import List, Union

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class CascadeEnsemble(EnsembleBase):
    """
    Ensemble method that iterates over the annotations and picks the first annotation that is not unannotated.
    """
    def run(self, annotations: List[Annotation]):
        for annotation in annotations:
            if not annotation.unannotated:
                return annotation
        return annotations[0]
