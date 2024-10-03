from abc import ABC
from typing import List, Tuple

from loguru import logger
from tqdm import tqdm

from dataloader.dataloader import DataLoaderBase
from entity.project import Project, Version
from execution.execution import ExecutionBase
from writer.writer import WriterBase


class PipelineBase(ABC):

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        pass

# TODO: Move to BATCH, and use the Execution pipeline
class BatchPipeline:
    def __init__(self, pipeline: ExecutionBase,
                 loader: DataLoaderBase,
                 writer: WriterBase,
                 cache_size=2):
        self.pipeline = pipeline
        self.loader = loader
        self.writer = writer
        self.cache_size = cache_size

    def run(self, projects_list: List) -> None:
        project_cache: List[Project] = []
        projects = self.loader.load(projects_list)
        for project in tqdm(projects):
            try:
                project = self.pipeline.run(project)
            except Exception as e:
                logger.info(f"Error processing {project.name}: {e} - Skipping project")
                continue

            print(project)

            project_cache.append(project)
            if len(project_cache) >= self.cache_size:
                self.writer.write_bulk(project_cache)
                project_cache = []
        if project_cache:
            self.writer.write_bulk(project_cache)