from entity.project import Project
from execution.execution import ExecutionBase
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from vcs.util import checkout
from vcs.version_strategy import VersionStrategyBase


class FileAnnotationExecution(ExecutionBase):
    def __init__(self,
                 identifier_extraction: IdentifierExtractionPipeline,
                 annotation_pipeline: FileAnnotationPipeline,
                 version_strategy: VersionStrategyBase,
                 ):
        self.identifier_extraction = identifier_extraction
        self.annotation_pipeline = annotation_pipeline
        self.version_strategy = version_strategy

    def run(self, project: Project) -> Project:
        project.versions = self.version_strategy.get_versions(project)

        for version in project.versions:
            checkout(project.dir_path, version.commit_id)

            project, version = self.identifier_extraction.run(project, version)
            project, version = self.annotation_pipeline.run(project, version)

        return project
