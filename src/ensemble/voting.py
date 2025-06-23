from typing import List, Tuple, Union

import numpy as np

from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class VotingEnsemble(EnsembleBase):
    def __init__(self, k=10):
        super().__init__()
        self.k = k

    def run(self, annotations: List[Annotation]) -> Annotation:
        best, n = self.extract_best(annotations)

        if not best:
            return Annotation(distribution=np.zeros(n).tolist(),
                              unannotated=1)

        distributions = np.zeros(n)
        for lf_top in best:
            for i, p in enumerate(lf_top):
                distributions[p] = distributions[p] + self.vote_weight(i)
        distributions = distributions / np.linalg.norm(distributions)
        return Annotation(distribution=distributions.tolist(),
                          unannotated=0)

    def extract_best(self, annotations: List[Annotation]):
        best = []
        n = 0
        for annotation in annotations:
            n = len(annotation.distribution)
            if not annotation.unannotated:
                top = np.argsort(annotation.distribution)[::-1][: self.k]
                best.append(top)
        return best, n

    def vote_weight(self, i):
        return self.k - i
