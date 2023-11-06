from abc import ABC
from typing import List, Union

import numpy as np


class EnsembleBase(ABC):
    """
    Base class for ensemble methods. Ensemble methods are used to combine the annotations of multiple annotators into
    a single annotation. The ensemble method is called with a list of annotations, where each annotation is a list of
    probabilities for each label. The ensemble method should return a single annotation, which is a list of probabilities
    for each label.
    """
    def __init__(self):
        pass

    def __call__(self, annotations: List[Union[np.array, List]], *args, **kwargs):
        return self.run(annotations)

    def run(self, annotations: List[Union[np.array, List]]):
        pass


class EnsembleNone(EnsembleBase):
    """
    Ensemble method that does not do anything. This is useful for single annotator experiments.
    """
    def run(self, annotations: List[Union[np.array, List]]):
        return annotations
