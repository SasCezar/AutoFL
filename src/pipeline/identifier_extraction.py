from typing import Dict

from entity.project import Project
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class IdentifierExtractionPipeline(PipelineBase):
    def __init__(self):
        self.parser_factory = ParserFactory()
        self.parsers: Dict[str, ParserBase] = {}

    def run(self, project: Project) -> Project:
        for file in project.files:
            file.identifiers = self.parsers[file.language].parse(file)

        return project
