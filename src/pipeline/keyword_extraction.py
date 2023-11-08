from typing import Tuple

from entity.project import Project, Version
from keyword_extraction.keyword_extraction import KeywordExtractionBase
from pipeline.pipeline import PipelineBase
from utils.utils import split_camelcase


class KeywordExtractionPipeline(PipelineBase):
    def __init__(self, keyword_extractor: KeywordExtractionBase, split_tokens: bool = False):
        self.keyword_extractor = keyword_extractor
        self.split_tokens = split_tokens

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        content = []
        for file in version.files:
            content.extend(file.identifiers)

        if self.split_tokens:
            content = [split_camelcase(x) for x in content]
        version.keywords = self.keyword_extractor.get_keywords(" ".join(content))

        return project, version
