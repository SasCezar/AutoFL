from typing import List

import numpy as np
from loguru import logger
from sklearn.metrics.pairwise import cosine_similarity

from embedding.embedding import AbstractEmbeddingModel
from entity.taxonomy import TaxonomyBase
from annotation import LFBase


class SimilarityLF(LFBase):
    """
    Labelling function that uses vector similarity to label examples.
    """
    def __init__(self, taxonomy: TaxonomyBase, embedding: AbstractEmbeddingModel):
        super().__init__(taxonomy)
        self.embedding = embedding
        self.label_vecs = self.embed_labels()
        self.content = False

    def annotate(self, name: str, content: str) -> np.array:
        content_vec = [self.embedding.get_embedding(content.lower())]

        try:
            sims = cosine_similarity(content_vec, self.label_vecs)
        except ValueError:
            logger.error(f"Error in {name}\nContent: {content}\nContent vec: {content_vec}")
            sims = np.zeros(len(self.label_vecs)) - 1

        # Adding 1 (-1 is the lowest value for cosine sim) to bring the vector in the range 0-1 when normalizing
        sims = sims[0] + 1
        norm = np.linalg.norm(sims)
        node_labels = sims / norm if norm else sims

        return node_labels

    def embed_labels(self) -> List[np.array]:
        res = []
        for label in self.taxonomy:
            res.append(self.embedding.get_embedding(label.name.lower()))

        return res
