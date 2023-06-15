from abc import ABC, abstractmethod

import numpy as np


class TransformationBase(ABC):
    @abstractmethod
    def transform(self, distribution: np.array):
        pass


class SingleLabel(TransformationBase):
    def transform(self, distribution: np.array):
        argmax = np.argmax(distribution)
        distribution = np.zeros(len(distribution))
        distribution[argmax] = 1
        return distribution


class TopLabels(TransformationBase):
    """
    Picks the probabilities with a
    """
    def __init__(self, top_k, min_threshold=0.05):
        self.top_k = top_k
        self.min_threshold = min_threshold

    def transform(self, distribution: np.array):
        sorted_distribution = np.argsort(distribution)[::-1]
        res_distribution = np.zeros(len(distribution))

        for i in sorted_distribution[:self.top_k]:
            res_distribution[i] = distribution[i] if distribution[i] > self.min_threshold else 0

        norm = np.linalg.norm(res_distribution)
        if norm != 0:
            res_distribution = res_distribution / norm
        return res_distribution
