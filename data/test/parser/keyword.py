from collections import Counter
import numpy as np
from multiset import Multiset
from entity.taxonomy import KeywordLabel
from annotation import LFBase


class KeywordLF(LFBase):

    def annotate(self, name: str, content: str) -> np.array:
        node_labels = np.zeros(len(self.taxonomy))
        for _label in self.taxonomy:
            label: KeywordLabel = _label
            intersection = list(label.keywords.intersection(Multiset(content.split())))
            intersection = Counter(intersection)
            node_labels[label.index] = sum([intersection[k] * label.weights[k]
                                            for k in intersection.keys()])

        norm = np.sum(node_labels)
        node_vec = node_labels / norm if norm > 0 else np.zeros(len(self.taxonomy))

        return node_vec
