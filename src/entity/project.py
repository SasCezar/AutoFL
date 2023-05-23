import json
from typing import List, Union, Iterable


class Project:
    def __int__(self, name: str, remote: str, languages: Union[str, List[str]], dir_path: str = '.'):
        self.name = name
        self.remote = remote
        self.dir_path = dir_path
        self.languages = languages

        self.files = []

    def clone(self):
        pass

    def load_files(self):
        pass

    def __iter__(self) -> Iterable:
        return FilesIterator(self.languages)

    @property
    def languages(self) -> List:
        return self._languages

    @languages.setter
    def languages(self, languages) -> Union[None, TypeError]:
        arg_type = type(languages)
        if arg_type not in [str, list]:
            return TypeError('Languages passed are not valid', languages)

        if arg_type == str:
            self._languages = [languages]
        elif arg_type == list:
            self._languages = languages

    def to_json(self) -> str:
        annotated_files = {}
        for file in self:
            annotated_files[file.name] = {'annot': file.annot, 'label': file.label}

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


class File:
    def __int__(self, path):
        self.path = path
        self.content = self._load_content()

    def _load_content(self) -> str:
        with open(self.path, 'rt') as inf:
            content = ' '.join(inf.readlines())

        return content
