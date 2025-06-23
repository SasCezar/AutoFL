from typing import List


from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class NoneEnsemble(EnsembleBase):
    """
    Ensemble method that does not do anything. This is useful for single annotator experiments.
    """

    def run(self, annotations: List[Annotation]) -> Annotation:
        return Annotation(distribution=annotations[0].distribution, unannotated=0)
