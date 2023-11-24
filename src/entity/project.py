from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any

from pydantic import BaseModel

from entity.file import File
from parser.extensions import Extension


class Version(BaseModel):
    """
    Class representing a version. Each version has a commit id (sha), a commit number describing the position of the
    commit in the project's history, a commit date and a map of files.
    """
    commit_id: str
    commit_num: int = None
    commit_date: datetime = None
    keywords: Optional[List[str]] = None
    files: Optional[Dict[str, File]] = None
    package_annotation: Optional[Dict[str, list]] = {}


class Project(BaseModel):
    """
    Class representing a project. Each project has a name, a remote (url), a directory path, a list of languages,
    a list of versions, a list of keywords, a taxonomy and a list of predicted labels and developer assigned labels.
    """
    name: str
    cfg: Optional[Dict[str, Any]] = None
    remote: Optional[str] = None
    dir_path: Optional[str] = None
    languages: Optional[List[str]] = None
    versions: Optional[List[Version]] = []
    taxonomy: Optional[Dict[str, str]] = None
    project_annotation: Optional[Dict[str, list]] = {}
    predicted_labels: Optional[List[str]] = None
    dev_labels: Optional[List[str]] = None


class VersionBuilder:
    """
    Class responsible for building a version from a given commit id and a list of languages.
    """

    def build_version(self, repo_dir: Path | str, languages: List[str], version: Version) -> Version:
        files = self.load_files(Path(repo_dir), languages)
        version.files = files
        return version

    def load_files(self, repo_dir: Path, languages: List[str]) -> Dict[str, File]:
        extensions = self.get_languages_ext(languages)
        all_paths = list(repo_dir.glob('**/*'))
        filtered_paths = [Path(x) for x in all_paths if x.is_file() and x.suffix.lower() in extensions]
        files = {}
        for path in filtered_paths:
            rel_path = str(path.relative_to(repo_dir))
            language = self.language_from_ext(path.suffix, languages)
            content = self.read_file(path)
            file = File(path=rel_path, language=language, content=content)
            files[rel_path] = file

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
