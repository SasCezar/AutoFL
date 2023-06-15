from typing import List

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from entity.taxonomy import TaxonomyBase
from annotation import LFBase


class SimilarityLF(LFBase):
    def __init__(self, taxonomy: TaxonomyBase, embedding):
        super().__init__(taxonomy)
        self.embedding = embedding
        self.label_vecs = self.embed_labels()
        self.content = False

    def annotate(self, name, content) -> np.array:
        content_vec = [self.embedding.get_embedding(content.lower())]

        try:
            sims = cosine_similarity(content_vec, self.label_vecs)
        except ValueError:
            print(f"Error in {name}")
            print(f"Content: {content}")
            print(f"Content vec: {content_vec}")

        # Adding -1 (lowest value for cosine sim) to bring the vector in the range 0-1 when normalizing
        sims = sims[0] + -1
        norm = np.linalg.norm(sims)
        node_labels = sims / norm if norm else sims

        return node_labels

    def embed_labels(self) -> List[np.array]:
        res = []
        for label in self.taxonomy:
            res.append(self.embedding.get_embedding(label.name.lower()))

        return res
