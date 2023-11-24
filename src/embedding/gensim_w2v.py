import re

import numpy
import numpy as np
from gensim.models import KeyedVectors
from embedding.embedding import AbstractEmbeddingModel


class W2VEmbedding(AbstractEmbeddingModel):
    """
    Class for embedding models using Word2Vec model.
    """

    def __init__(self, path: str, model: str = 'W2V-Unk', split_camel: bool = False):
        super().__init__(split_camel)
        self._name = f'{model}'
        self.model = KeyedVectors.load_word2vec_format(path, binary=True)

    def get_embedding(self, text: str) -> numpy.ndarray:
        """
        Returns the embedding of the text.
        :param text:
        :return:
        """
        embeddings = []
        if not text:
            embeddings.append(np.zeros(self.model.vector_size))
        for word in self.split(str(text)):
            if word in self.model:
                embeddings.append(self.model[word])
            else:
                embeddings.append(np.zeros(self.model.vector_size))
        return numpy.mean(embeddings, axis=0)
