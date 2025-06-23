from typing import Dict, Tuple

from entity.project import Project, Version
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class IdentifierExtractionPipeline(PipelineBase):
    def __init__(self, languages_path, force: bool = False):
        self.parser_factory = ParserFactory
        self.parsers: Dict[str, ParserBase] = {}
        self.force = force
        self.languages_path = languages_path

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        for file_name in version.files:
            file = version.files[file_name]
            lang = file.language.strip(".")

            if file.identifiers and not self.force:
                continue

            if lang not in self.parsers:
                self.parsers[lang] = self.parser_factory.create_parser(
                    lang, self.languages_path
                )

            identifiers, package = self.parsers[lang].parse(file)
            file.identifiers = identifiers
            file.package = package

        return project, version
