import numpy

from embedding.embedding import AbstractEmbeddingModel


class BERTEmbedding(AbstractEmbeddingModel):
    """
    Class for embedding models using BERT.
    """

    def __init__(self, model, split_camel: bool = False):
        super().__init__(split_camel=split_camel)
        self._name = f'{model}'
        self.model = spacy.load(model, disable=["ner", "textcat", "parser"])

    def get_embedding(self, text: str) -> numpy.ndarray:
        """
        Returns the embedding of the text.
        :param text:
        :return:
        """
        if self._split_camel:
            text = ' '.join(self.split(text))
        return self.model(text).vector
