import fasttext as ft
import numpy

from embedding.embedding import AbstractEmbeddingModel


class FastTextEmbedding(AbstractEmbeddingModel):
    """
    Class for embedding models using FastText model.
    """

    def __init__(self, path: str, model: str = 'fastText', split_camel: bool = False):
        super().__init__(split_camel=split_camel)
        self._name = f'{model}'
        self.model = ft.load_model(path)

    def get_embedding(self, text: str) -> numpy.ndarray:
        """
        Returns the embedding of the text.
        :param text:
        :return:
        """
        if self._split_camel:
            text = ' '.join(self.split(text))
        return self.model.get_sentence_vector(text)
