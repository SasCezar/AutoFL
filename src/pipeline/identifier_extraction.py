from typing import Dict, Tuple

from entity.project import Project, Version
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class IdentifierExtractionPipeline(PipelineBase):
    def __init__(self, languages_path, use_cache: bool = False):
        self.parser_factory = ParserFactory
        self.parsers: Dict[str, ParserBase] = {}
        self.use_cache = use_cache
        self.languages_path = languages_path

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        for file in version.files:
            lang = file.language.strip('.')

            if file.identifiers or self.use_cache:
                continue

            if lang not in self.parsers:
                self.parsers[lang] = self.parser_factory.create_parser(lang, self.languages_path)

            file.identifiers = self.parsers[lang].parse(file)

        return project, version
