from typing import Tuple

import numpy as np

from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class ProjectAnnotationPipeline(PipelineBase):
    def __init__(self):
        pass

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        project_dist = []
        for file_name in version.files:
            file = version.files[file_name]
            if file.annotation.unannotated:
                continue
            project_dist.append(file.annotation.distribution)

        project.project_annotation[version.commit_id] = list(np.mean(project_dist, axis=0))

        return project, version
