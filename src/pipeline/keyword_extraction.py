from typing import Tuple

from entity.project import Project, Version
from keyword_extraction.keyword_extraction import KeywordExtractionBase
from pipeline.pipeline import PipelineBase


class KeywordExtractionPipeline(PipelineBase):
    def __init__(self, keyword_extractor: KeywordExtractionBase):
        self.keyword_extractor = keyword_extractor

    def run(self, project: Project, version: Version) -> Tuple[Project, Version]:
        content = []
        for file in version.files:
            content.extend(file.identifiers)

        version.keywords = self.keyword_extractor.get_keywords(" ".join(content))

        return project, version
