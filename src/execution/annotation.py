from typing import List

from loguru import logger

from entity.project import Project, VersionBuilder, Version
from execution.execution import ExecutionBase
from pipeline.file_annotation import FileAnnotationPipeline
from pipeline.identifier_extraction import IdentifierExtractionPipeline
from pipeline.package_annotation import PackageAnnotationPipeline
from pipeline.project_annotation import ProjectAnnotationPipeline
from vcs.latest import LatestVersionStrategy
from vcs.vcs import VCS
from vcs.version_strategy import VersionStrategyBase


class AnnotationExecution(ExecutionBase):
    def __init__(self,
                 identifier_extraction_pipeline: IdentifierExtractionPipeline,
                 file_annotation_pipeline: FileAnnotationPipeline | None = None,
                 package_annotation_pipeline: PackageAnnotationPipeline | None = None,
                 project_annotation_pipeline: ProjectAnnotationPipeline | None = None,
                 version_strategy: VersionStrategyBase = None,
                 vcs: VCS = None
                 ):
        self.identifier_extraction_pipeline = identifier_extraction_pipeline
        self.file_annotation_pipeline = file_annotation_pipeline
        self.package_annotation_pipeline = package_annotation_pipeline
        self.project_annotation_pipeline = project_annotation_pipeline
        self.version_strategy = version_strategy if version_strategy else LatestVersionStrategy()
        self.vcs = vcs if vcs else VCS()
        self.version_builder = VersionBuilder()

    def run(self, project: Project) -> Project:
        repo = self.vcs.init(project)

        versions: List[Version] = self.version_strategy.get_versions(repo)
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

            if self.file_annotation_pipeline:
                project, version = self.file_annotation_pipeline.run(project, version)

            if self.package_annotation_pipeline:
                project, version = self.package_annotation_pipeline

            if self.project_annotation_pipeline:
                project, version = self.project_annotation_pipeline

        return project
