from typing import List


from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation


class CascadeEnsemble(EnsembleBase):
    """
    Ensemble method that iterates over the annotations and picks the first annotation that is not unannotated.
    """

    def run(self, annotations: List[Annotation]) -> Annotation:
        for annotation in annotations:
            if not annotation.unannotated:
                return Annotation(distribution=annotation.distribution,
                                  unannotated=0)

        return Annotation(distribution=annotations[0].distribution, unannotated=1)
