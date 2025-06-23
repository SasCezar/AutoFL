import json
from pathlib import Path
from typing import List

from entity.project import Project
from writer.writer import WriterBase


class FileWriter(WriterBase):
    def __init__(self, out_path: str | Path, exclude: str, indent: None | int = None):
        """
        :param out_path:
        :param exclude: String of a dict of fields to exclude
        :param indent:
        """
        super().__init__()
        self.out_path = Path(out_path)
        self.out_path.mkdir(parents=True, exist_ok=True)
        self.exclude = json.loads(exclude) if exclude else {}
        self.indent = indent

    def write(self, project: Project):
        project_dict = project.model_dump_json(exclude=self.exclude, indent=self.indent)

        out_file = self.out_path.joinpath(f"{project.name}.json")

        with open(out_file, "wt") as outf:
            outf.write(project_dict)

    def write_bulk(self, projects: List[Project]):
        for project in projects:
            self.write(project)
