from typing import Tuple

import numpy as np
from tqdm import tqdm

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.annotation import Annotation
from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class FileAnnotationPipeline(PipelineBase):
    def __init__(self,
                 lf: LFBase,
                 filtering: FilteringBase,
                 transformation: TransformationBase):
        self.lf = lf
        self.filtering = filtering
        self.transformation = transformation

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        res = {}
        for file in tqdm(version.files, desc=f"Labelling files for {project.name} @ version: {version.commit_id}"):

            label_vec = self.lf.annotate(file.path, " ".join(file.identifiers))
            unannotated = 0

            if self.filtering:
                unannotated = self.filtering.filter(label_vec)

            if self.transformation and not unannotated:
                label_vec = self.transformation.transform(label_vec)

            if not np.linalg.norm(label_vec):
                unannotated = 1

            res[file.path] = (Annotation(distribution=list(label_vec), labels=[], unannotated=unannotated))

        version.files_annotation = res
        return project, version
