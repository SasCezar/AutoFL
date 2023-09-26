from abc import ABC
from pathlib import Path
from typing import List, Tuple

from tqdm import tqdm

from entity.project import Project, Version
from execution.execution import ExecutionBase


class PipelineBase(ABC):

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        pass


# TODO: Move to BATCH, and use the Execution pipeline
class BatchPipeline:
    def __init__(self, pipeline: ExecutionBase,
                 out_path: str | Path,
                 exclude=None):
        self.pipeline = pipeline
        self.out_path = Path(out_path)
        self.out_path.mkdir(parents=True, exist_ok=True)
        if exclude is None:
            exclude = {}
        self.exclude = exclude

    def run(self, projects: List[Project]) -> None:
        for project in tqdm(projects):
            project = self.pipeline.run(project)
            project_dict = project.model_dump_json(exclude=self.exclude)

            out_file = self.out_path.joinpath(f'{project.name}.json')

            with open(out_file, 'wt') as outf:
                outf.write(project_dict)
