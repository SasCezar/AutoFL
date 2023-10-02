from abc import ABC
from pathlib import Path
from typing import List, Tuple

from tqdm import tqdm

from entity.project import Project, Version
from execution.execution import ExecutionBase
from writer.writer import WriterBase


class PipelineBase(ABC):

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        pass


# TODO: Move to BATCH, and use the Execution pipeline
class BatchPipeline:
    def __init__(self, pipeline: ExecutionBase,
                 writer: WriterBase,
                 cache_size=500):
        self.pipeline = pipeline
        self.writer = writer
        # if exclude is None:
        #     exclude = {}
        # self.exclude = exclude

    def run(self, projects: List[Project]) -> None:
        project_cache: List[Project] = []
        for project in tqdm(projects):
            project = self.pipeline.run(project)
            if len(project_cache) >= self.cache_size:
                self.writer.write_bulk(project_cache)
