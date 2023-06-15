from abc import ABC, abstractmethod

import numpy as np
from scipy.spatial.distance import jensenshannon


class FilteringBase(ABC):
    @abstractmethod
    def filter(self, distribution: np.array):
        pass


class JSDFiltering(FilteringBase):
    def __init__(self, threshold):
        self.threshold = threshold

    def filter(self, distribution: np.array):
        n = len(distribution)
        uniform_vec = np.ones(n) / n

        if np.linalg.norm(distribution) == 0 or jensenshannon(distribution, uniform_vec) <= self.threshold:
            return 1

        return 0


class ThresholdFiltering(FilteringBase):
    def __init__(self, threshold):
        self.threshold = threshold

    def filter(self, distribution: np.array):
        if np.linalg.norm(distribution) == 0 or np.max(distribution) <= self.threshold:
            return 0

        return 1


