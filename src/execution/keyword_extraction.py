from loguru import logger

from entity.project import Project, VersionBuilder
from execution.execution import ExecutionBase
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.keyword_extraction import KeywordExtractionPipeline
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class KeywordExtractionExecution(ExecutionBase):
    def __init__(self,
                 identifier_extraction_pipeline: IdentifierExtractionPipeline,
                 keyword_extraction_pipeline: KeywordExtractionPipeline,
                 version_strategy: VersionStrategyBase,
                 vcs: VCS
                 ):
        self.identifier_extraction_pipeline = identifier_extraction_pipeline
        self.keyword_extraction_pipeline = keyword_extraction_pipeline
        self.version_strategy = version_strategy
        self.vcs = vcs
        self.version_builder = VersionBuilder()

    def run(self, project: Project) -> Project:
        repo = self.vcs.init(project)

        versions = self.version_strategy.get_versions(repo)
        logger.info(f'Found {len(versions)} versions for project {project.name}')

        if not versions:
            logger.info('No versions found')
            return project

        for version in versions:
            logger.info(f'Analyzing version {version.commit_id}')
            self.vcs.checkout(repo, version.commit_id)
            version = self.version_builder.build_version(project.dir_path, project.languages, version)

            project.versions.append(version)

            project, version = self.identifier_extraction_pipeline.run(project, version)
            project, version = self.keyword_extraction_pipeline.run(project, version)

        return project
