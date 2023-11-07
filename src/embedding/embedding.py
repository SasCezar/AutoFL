import re
from abc import ABC, abstractmethod

import numpy


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
            return re.sub(
                '([A-Z][a-z]+)|_', r' \1', re.sub('([A-Z]+)', r' \1', name)
            ).split()

        return name.split('')
