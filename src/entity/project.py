from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel

from entity.annotation import Annotation
from entity.file import File


class Version(BaseModel):
    commit_id: str
    files: Optional[List[File]]
    files_annotation: Optional[List[Annotation]]
    labels: Optional[List[str]]


class Project(BaseModel):
    name: str
    remote: Optional[str]
    dir_path: Optional[Path]
    languages: Optional[List[str]]
    versions: Optional[List[Version]] = []
    keywords: Optional[List[str]]
    labels: Optional[List[str]]


class VersionBuilder:
    def build_version(self, repo_dir, commit_id, languages):
        files = self.load_files(repo_dir, languages)

        return Version(commit_id=commit_id, files=files)

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
