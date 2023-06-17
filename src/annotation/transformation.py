from abc import ABC, abstractmethod

import numpy as np


class TransformationBase(ABC):
    @abstractmethod
    def transform(self, distribution: np.array) -> np.array:
        pass


class SingleLabel(TransformationBase):
    def transform(self, distribution: np.array) -> np.array:
        argmax = np.argmax(distribution)
        distribution = np.zeros(len(distribution))
        distribution[argmax] = 1
        return distribution


class TopLabels(TransformationBase):
    """
    Picks the probabilities with a threshold higher than min_threshold
    """

    def __init__(self, min_threshold: float = 0.05):
        self.min_threshold = min_threshold

    def transform(self, distribution: np.array) -> np.array:
        res_distribution = distribution > self.min_threshold

        norm = np.linalg.norm(res_distribution)
        if norm != 0:
            res_distribution = res_distribution / norm
        return res_distribution
