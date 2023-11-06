from typing import Tuple

from entity.project import Project, Version
from pipeline.pipeline import PipelineBase


class ProjectAnnotationPipeline(PipelineBase):
    def __init__(self):
        pass

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        return project, version
