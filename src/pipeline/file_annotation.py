from typing import Dict

import numpy as np
from tqdm import tqdm

from annotation import LFBase
from annotation.filtering import FilteringBase
from annotation.transformation import TransformationBase
from entity.annotation import Annotation
from entity.file import File
from entity.project import Project
from parser.parser import ParserFactory, ParserBase
from pipeline.pipeline import PipelineBase


class FileAnnotationPipeline(PipelineBase):
    def __init__(self,
                 lf: LFBase,
                 filtering: FilteringBase,
                 transformation: TransformationBase):
        self.parser_factory = ParserFactory()
        self.parsers: Dict[str, ParserBase] = {}
        self.lf = lf
        self.filtering = filtering
        self.transformation = transformation

    def run(self, project: Project) -> Project:
        res = []
        for file in tqdm(project.files):

            content = self.parse_file(file) if self.lf.content else ""

            label_vec = self.lf.annotate(file.path, content)
            unannotated = 0

            if self.filtering:
                unannotated = self.filtering.filter(label_vec)

            if self.transformation and not unannotated:
                label_vec = self.transformation.transform(label_vec)

            if not np.linalg.norm(label_vec):
                unannotated = 1

            res.append(Annotation(file=file.path, distribution=list(label_vec), labels=[], unannotated=unannotated))

        project.files_annotation = res
        return project

    def parse_file(self, file: File):
        lang = file.language.strip('.')
        if lang not in self.parsers:
            self.parsers[lang] = self.parser_factory.create_parser(lang)
        content = " ".join(self.parsers[lang].parse(file))
        return content
