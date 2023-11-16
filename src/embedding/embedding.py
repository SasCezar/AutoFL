from abc import ABC, abstractmethod

import numpy

from utils.utils import split_camelcase


class AbstractEmbeddingModel(ABC):
    """
    Abstract class for embedding models.
    """

    def __init__(self, split_camel: bool = False):
        self._name = 'AbstractEmbeddingModel'
        self.model = None
        self._split_camel = split_camel

    @abstractmethod
    def get_embedding(self, text: str) -> numpy.ndarray:
        pass

    def split(self, name: str):
        if self._split_camel:
            return split_camelcase(name)
        return name.split(' ')
