import glob
import json
from pathlib import Path
from typing import List, Union, Iterable

from entity.file import File


class Project:
    def __init__(self, name: str, remote: str, extensions: Union[str, List[str]], dir_path: str = '.'):
        self.name = name
        self.remote = remote
        self.dir_path = dir_path
        self.extensions = extensions

        self.files = self.load_files()

    def clone(self):
        pass

    def load_files(self):
        all_paths = glob.glob(self.dir_path, recursive=True)
        filtered_paths = [Path(x) for x in all_paths if x in [f'*.{ext}' for ext in self.extensions]]

        return [File(path) for path in filtered_paths]

    def __iter__(self) -> Iterable:
        return FilesIterator(self.files)

    @property
    def extensions(self) -> List[File]:
        return self._languages

    @extensions.setter
    def extensions(self, languages):
        arg_type = type(languages)
        if arg_type not in [str, list]:
            raise TypeError('Languages passed are not valid', languages)

        if arg_type == str:
            self._languages = [languages]
        elif arg_type == list:
            self._languages = languages

    def to_json(self) -> str:
        annotated_files = {}
        for file in self:
            annotated_files[file.name] = {'annot': file.annot, 'label': file.name}

        return json.dumps(annotated_files)


class FilesIterator:
    def __init__(self, files):
        self.idx = 0
        self.files = files

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        try:
            return self.files[self.idx - 1]
        except IndexError:
            self.idx = 0
            raise StopIteration
