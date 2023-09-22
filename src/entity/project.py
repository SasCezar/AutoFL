from pathlib import Path
from typing import List, Optional, Dict, Union

from pydantic import BaseModel

from entity.annotation import Annotation
from entity.file import File
from parser.extensions import Extension


class Version(BaseModel):
    commit_id: str
    files: Optional[List[File]] = None
    files_annotation: Optional[Dict[str, Annotation]] = None
    files_packages: Optional[Dict[Union[str | Path], Union[str | Path]]] = None


class Project(BaseModel):
    name: str
    remote: Optional[str] = None
    dir_path: Optional[Path] = None
    languages: Optional[List[str]] = None
    versions: Optional[List[Version]] = []
    keywords: Optional[List[str]] = None
    taxonomy: Optional[Dict[int, str]] = None
    predicted_labels: Optional[List[str]] = None
    dev_labels: Optional[List[str]] = None


class VersionBuilder:
    def build_version(self, repo_dir, commit_id, languages):
        files = self.load_files(repo_dir, languages)

        return Version(commit_id=commit_id, files=files)

    def load_files(self, repo_dir: Path, languages: List[str]) -> List[File]:
        extensions = self.get_languages_ext(languages)
        all_paths = list(repo_dir.glob('**/*'))
        filtered_paths = [Path(x) for x in all_paths if x.is_file() and x.suffix.lower() in extensions]
        files = []
        for path in filtered_paths:
            rel_path = path.relative_to(repo_dir)
            language = self.language_from_ext(path.suffix, languages)
            content = self.read_file(path)
            file = File(path=rel_path, language=language, content=content)
            files.append(file)

        return files

    @staticmethod
    def read_file(path: Path) -> str:
        try:
            with open(path, 'rt') as inf:
                content = ' '.join(inf.readlines())
        except:
            with open(path, 'rt', encoding='windows-1252') as inf:
                content = ' '.join(inf.readlines())

        return content

    @staticmethod
    def get_languages_ext(languages):
        extensions = set()
        for lang in languages:
            exts = Extension[lang.lower()].value
            extensions.update(exts)

        return extensions

    @staticmethod
    def language_from_ext(extension, languages):
        for lang in languages:
            if extension in Extension[lang.lower()].value:
                return lang
