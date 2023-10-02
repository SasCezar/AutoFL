from typing import List

from entity.project import Project
from writer.writer import WriterBase


class FileWriter(WriterBase):
    def __init__(self, out_path, exclude):
        super().__init__()
        self.out_path = out_path
        self.exclude = exclude

    def write(self, project: Project):
        project_dict = project.model_dump_json(exclude=self.exclude)

        out_file = self.out_path.joinpath(f'{project.name}.json')

        with open(out_file, 'wt') as outf:
            outf.write(project_dict)

    def write_bulk(self, projects: List[Project]):
        for project in projects:
            self.write(project)
