from typing import Dict, List

from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.annotation import Annotation
from entity.file import File
from entity.project import Project
from annotation import LFBase
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class FileAnnotationPipeline(PipelineBase):
    def __init__(self, lf: LFBase, filtering: FilteringBase, transformation: TransformationBase):
        self.parser_factory = ParserFactory()
        self.parsers: Dict[str, ParserBase] = {}
        self.lf = lf
        self.filtering = filtering
        self.transformation = transformation

    def run(self, project: Project) -> Project:
        res = []
        for file in project.files:

            content = self.parse_file(file) if self.lf.content else ""

            label_vec, labels = self.lf.annotate(file.path, content)
            filtered = 0

            if self.filtering:
                filtered = self.filtering.filter(label_vec)

            if self.transformation:
                label_vec = self.transformation.transform(label_vec)

            res.append(Annotation(file=file.path, distribution=label_vec, labels=labels, filtered=filtered))

        project.files_annotation = res
        return project

    def parse_file(self, file: File):
        lang = file.language
        if lang not in self.parsers:
            self.parsers[lang] = self.parser_factory.create_parser(lang)
        content = " ".join(self.parsers[lang].parse(file))
        return content
