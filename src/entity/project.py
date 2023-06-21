import os
from pathlib import Path
from typing import List, Union, Optional

from git import Repo
from pydantic import BaseModel

from entity.annotation import Annotation
from entity.file import File


class Project(BaseModel):
    name: str
    remote: str
    dir_path: Path
    languages: List[str]
    files: List[File]
    files_annotation: Optional[List[Annotation]]
    sha: Optional[str]
    labels: Optional[List[str]]


class ProjectBuilder:
    def build(self,
              name: str,
              directory: Union[str, Path],
              languages: Union[str, List[str]],
              remote: Optional[str] = None
              ) -> Project:

        repo_dir = Path(directory, name)

        if remote:
            self.clone(remote, repo_dir)

        repo = Repo(repo_dir)
        sha = repo.head.object.hexsha

        files = self.load_files(repo_dir, languages)

        return Project(name=name, remote=remote, dir_path=repo_dir, languages=languages, files=files, sha=sha)

    @staticmethod
    def clone(remote: str, repo_dir: Path) -> None:
        if not os.path.exists(repo_dir):
            Repo.clone_from(remote, repo_dir)

        return

    def load_files(self, repo_dir: Path, languages: List[str]) -> List[File]:
        all_paths = list(repo_dir.glob('**/*'))
        filtered_paths = [Path(x) for x in all_paths if x.is_file() and x.suffix.strip('.') in languages]
        files = []
        for path in filtered_paths:
            rel_path = path.relative_to(repo_dir)
            language = path.suffix
            content = self.read_file(path)
            file = File(path=rel_path, language=language, content=content)
            files.append(file)

        return files

    @staticmethod
    def read_file(path: Path) -> str:
        with open(path, 'rt') as inf:
            content = ' '.join(inf.readlines())

        return content
