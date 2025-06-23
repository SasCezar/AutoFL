import numpy as np

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.annotation import Annotation


class Annotator:
    """
    Class that performs the annotation of a file.
    """
    def __init__(self, lf: LFBase, filtering: FilteringBase,
                 transformation: TransformationBase, name: str = None):
        """

        :param lf: Labelling function to be used to annotate the files.
        :param filtering: Filtering strategy to be used to mark as unannotated files with noisy annotations.
        :param transformation: Transformation to apply to the annotation vector.
        """
        self.lf = lf
        self.filtering = filtering
        self.transformation = transformation
        self.name = name

    def annotate(self, name: str, content: str) -> Annotation:

        label_vec = self.lf.annotate(name, content)

        unannotated = False
        if self.filtering:
            unannotated = self.filtering.filter(label_vec)

        raw_vec = label_vec.copy()
        if self.transformation and not unannotated:
            label_vec = self.transformation.transform(label_vec)

        if not np.linalg.norm(label_vec):
            unannotated = 1

        annotation = Annotation(distribution=list(label_vec), unannotated=unannotated, raw_annotation=raw_vec)
        return annotation
