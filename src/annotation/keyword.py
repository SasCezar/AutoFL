from collections import Counter

import numpy as np
from multiset import Multiset

from entity.taxonomy import KeywordLabel, TaxonomyBase
from annotation import LFBase


class KeywordLF(LFBase):
    """
    Labelling function that uses identifiers and keywords.
    """

    def __init__(self, taxonomy: TaxonomyBase, key: str):
        super().__init__(taxonomy)
        self.key = key

    def annotate(self, name: str, content: str) -> np.array:
        """
        Compute the probability for the file given the name and/or the content.

        :param name: Source file name
        :param content: Content of the file (usually identifiers)
        :return:
        """
        node_labels = np.zeros(len(self.taxonomy))
        for _label in self.taxonomy:
            label: KeywordLabel = _label
            intersection = list(label.keywords[self.key].intersection(Multiset(content.split())))
            intersection = Counter(intersection)
            node_labels[label.index] = sum([intersection[k] * label.weights[self.key][k]
                                            for k in intersection.keys()])

        norm = np.sum(node_labels)
        node_vec = node_labels / norm if norm > 0 else np.zeros(len(self.taxonomy))

        return node_vec
