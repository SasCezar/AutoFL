from abc import ABC
from typing import List, Union, Tuple

import numpy as np

from entity.annotation import Annotation


class EnsembleBase(ABC):
    """
    Base class for ensemble methods. Ensemble methods are used to combine the annotations of multiple annotators into
    a single annotation. The ensemble method is called with a list of annotations, where each annotation is a list of
    probabilities for each label. The ensemble method should return a single annotation, which is a list of probabilities
    for each label.
    """

    def __init__(self):
        pass

    def __call__(self, annotations: List[Union[np.array, Annotation]], *args, **kwargs) \
            -> Tuple[Union[List | np.array], int]:
        """
        Making the ensemble method callable allows to also define functions as ensemble methods instead of classes. This
        is useful for ensemble methods that do not have any state.
        :param annotations:
        :param args:
        :param kwargs:
        :return:
        """
        distributions, unannotated = self.run(annotations)
        return self.normalize(distributions), unannotated

    def run(self, annotations: List[Annotation]) -> Tuple[Union[List | np.array], int]:
        """
        Run the ensemble method. This method should be implemented by subclasses.
        The ensemble method is called with a list of annotations, where each annotation is a list of probabilities for
        each label. The ensemble method should return a single annotation, which is a list of probabilities for each
        label. The ensemble method should also return a boolean indicating whether the ensemble method was able to
        produce a valid annotation. If the ensemble method was not able to produce a valid annotation, the ensemble
        method should return the first annotation in the list of annotations.
        :param annotations:
        :return:
        """
        pass

    @staticmethod
    def normalize(annotations: np.array) -> np.array:
        """
        Normalize the annotations. This method is used to bring the ensemble result into probability vectors.
        :param annotations:
        :return:
        """
        return np.array(annotations) / np.linalg.norm(annotations)

