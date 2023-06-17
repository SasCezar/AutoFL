from abc import ABC, abstractmethod

import numpy as np
from scipy.spatial.distance import jensenshannon


class FilteringBase(ABC):
    @abstractmethod
    def filter(self, distribution: np.array) -> bool:
        pass


class JSDFiltering(FilteringBase):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def filter(self, distribution: np.array) -> bool:
        n = len(distribution)
        uniform_vec = np.ones(n) / n

        if np.linalg.norm(distribution) == 0 or jensenshannon(distribution, uniform_vec) <= self.threshold:
            return True

        return False


class ThresholdFiltering(FilteringBase):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def filter(self, distribution: np.array) -> bool:
        if np.linalg.norm(distribution) == 0 or np.max(distribution) <= self.threshold:
            return False

        return True


