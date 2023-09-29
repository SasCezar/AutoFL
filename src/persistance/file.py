from abc import ABC

from entity.project import Project


class FileWriter(ABC):
    def __init__(self, out_path, exclude):
        self.out_path = out_path
        self.exclude = exclude

    def write(self, project: Project):
        project_dict = project.model_dump_json(exclude=self.exclude)

        out_file = self.out_path.joinpath(f'{project.name}.json')

        with open(out_file, 'wt') as outf:
            outf.write(project_dict)
