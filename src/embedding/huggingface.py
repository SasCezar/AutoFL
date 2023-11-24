import numpy
import torch

from embedding.embedding import AbstractEmbeddingModel
from sentence_transformers import SentenceTransformer
from transformers import BertModel, BertTokenizer


class HuggingFaceEmbedding(AbstractEmbeddingModel):
    """
    Class for embedding models using HuggingFace.
    """

    def __init__(self, name, model, split_camel: bool = False):
        super().__init__(split_camel=split_camel)
        self._name = f'{name}'
        do_lower_case = True
        self.model = BertModel.from_pretrained(model)
        self.tokenizer = BertTokenizer.from_pretrained(model, do_lower_case=do_lower_case)

    def get_embedding(self, text: str) -> numpy.ndarray:
        """
        Returns the embedding of the text.
        :param text:
        :return:
        """
        if self._split_camel:
            text = ' '.join(self.split(text))
        input_ids = torch.tensor(self.tokenizer.encode(text)).unsqueeze(0)  # Batch size 1
        outputs = self.model(input_ids)
        last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
        return last_hidden_states.mean(1).detach().numpy()[0]


class SentenceTransformersEmbedding(AbstractEmbeddingModel):
    def __init__(self, name, model, device='cpu', split_camel: bool = False):
        super().__init__(split_camel=split_camel)
        self._name = f'{name}'
        self.model = SentenceTransformer(model, device=device)
        self.model.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    def get_embedding(self, text: str) -> numpy.ndarray:
        """
        Returns the embedding of the text.
        :param text:
        :return:
        """
        if self._split_camel:
            text = ' '.join(self.split(text))
        embeddings = self.model.encode(text)
        return embeddings
