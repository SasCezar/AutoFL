from typing import Tuple, List, Union

import numpy as np
from tqdm import tqdm

from annotation.annotator import Annotator
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from ensemble.ensemble import EnsembleBase
from entity.annotation import Annotation
from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class FileAnnotationPipeline(PipelineBase):
    def __init__(self,
                 annotators: List[Annotator],
                 ensemble: Union[EnsembleBase, callable]):
        self.annotators = annotators
        self.ensemble = ensemble

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        res = {}

        for file in tqdm(version.files, desc=f"Labelling files for {project.name} @ version: {version.commit_id}"):
            file_label_vecs = []
            lfs_unannotated = []
            for annotator in self.annotators:
                label_vec, unannotated = annotator.annotate(file.path, " ".join(file.identifiers))
                lfs_unannotated.append(unannotated)
                file_label_vecs.append(label_vec)

            unannotated = bool(all(lfs_unannotated))

            label_vec = self.ensemble(file_label_vecs)
            if label_vec is None:
                print(label_vec)
            res[str(file.path)] = Annotation(distribution=list(label_vec), labels=[], unannotated=unannotated)

        version.files_annotation = res
        return project, version
