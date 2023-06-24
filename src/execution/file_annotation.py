from loguru import logger

from entity.project import Project, VersionBuilder
from execution.execution import ExecutionBase
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class FileAnnotationExecution(ExecutionBase):
    def __init__(self,
                 identifier_extraction: IdentifierExtractionPipeline,
                 annotation_pipeline: FileAnnotationPipeline,
                 version_strategy: VersionStrategyBase,
                 vcs: VCS
                 ):
        self.identifier_extraction = identifier_extraction
        self.annotation_pipeline = annotation_pipeline
        self.version_strategy = version_strategy
        self.vcs = vcs
        self.version_builder = VersionBuilder()

    def run(self, project: Project) -> Project:
        repo = self.vcs.init(project)

        version_ids = self.version_strategy.get_versions(repo)
        logger.info(f'Found {len(version_ids)} versions for project {project.name}')

        if not version_ids:
            logger.info('No versions found')
            return project

        for version_id in version_ids:
            logger.info(f'Analyzing version {version_id}')
            self.vcs.checkout(repo, version_id)
            version = self.version_builder.build_version(project.dir_path, version_id, project.languages)

            project.versions.append(version)

            project, version = self.identifier_extraction.run(project, version)
            project, version = self.annotation_pipeline.run(project, version)

        return project
