from abc import ABC
from typing import Dict

from entity.project import Project
from lf import LFBase
from parser.parser import ParserFactory, ParserBase


class PipelineBase(ABC):
    pass


class FileAnnotationPipeline(PipelineBase):
    def __init__(self, lf: LFBase):

        self.parser_factory = ParserFactory()
        self.parsers: Dict[str, ParserBase] = {}

        self.lf = lf

    def run(self, project: Project):
        res = {}
        for file in project:
            lang = file.language
            content = ""
            if self.lf.content:
                if lang not in self.parsers:
                    self.parsers[lang] = self.parser_factory.create_parser(lang)
                content = " ".join(self.parsers[lang].parse(file))

            label_vec = self.lf.annotate(file.path, content)
            res[file.path] = label_vec

        return res