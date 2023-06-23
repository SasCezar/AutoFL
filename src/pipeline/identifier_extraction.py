from typing import Dict, Tuple

from entity.project import Project, Version
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class IdentifierExtractionPipeline(PipelineBase):
    def __init__(self):
        self.parser_factory = ParserFactory()
        self.parsers: Dict[str, ParserBase] = {}

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        for file in version.files:
            file.identifiers = self.parsers[file.language].parse(file)

        return project, version
