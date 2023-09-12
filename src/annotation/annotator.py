import numpy as np

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase


class Annotator:
    def __init__(self, lf: LFBase, filtering: FilteringBase,
                 transformation: TransformationBase):
        self.lf = lf
        self.filtering = filtering
        self.transformation = transformation

    def annotate(self, name: str, content: str) -> np.array:

        label_vec = self.lf.annotate(name, content)

        if self.filtering:
            unannotated = self.filtering.filter(label_vec)

        if self.transformation and not unannotated:
            label_vec = self.transformation.transform(label_vec)

        if not np.linalg.norm(label_vec):
            unannotated = 1

        return label_vec, unannotated
