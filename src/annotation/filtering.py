from abc import ABC, abstractmethod

import numpy as np
from scipy.spatial.distance import jensenshannon


class FilteringBase(ABC):
    """
    Base class for annotation filtering.
    """

    @abstractmethod
    def filter(self, distribution: np.array) -> bool:
        """
        Given a numpy array representing a distribution, return a boolean on whether the annotation
        is filtered or not.
        :param distribution:
        :return:
        """
        pass


class JSDFiltering(FilteringBase):
    """
    Filters the annotation using the JSD between it and a uniform distribution.
    If the score is lower than a threshold (noisy annotation), the annotation is filtered.
    """

    def __init__(self, threshold: float):
        """

        :param threshold: JSD threshold used to filter the file
        """
        self.threshold = threshold

    def filter(self, distribution: np.array) -> bool:
        n = len(distribution)
        uniform_vec = np.ones(n) / n

        if (
            np.linalg.norm(distribution) == 0
            or jensenshannon(distribution, uniform_vec) <= self.threshold
        ):
            return True

        return False


class ThresholdFiltering(FilteringBase):
    """
    Filter based on the probability of the most likely class.
    If is not high enough, then the annotation is filtered.
    """

    def __init__(self, threshold: float):
        """
        :param threshold: Noise threshold used to filter the file
        """
        self.threshold = threshold

    def filter(self, distribution: np.array) -> bool:
        if np.linalg.norm(distribution) == 0 or np.max(distribution) <= self.threshold:
            return False

        return True
