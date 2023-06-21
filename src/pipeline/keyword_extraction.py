from entity.project import Project
from keyword_extraction.keyword_extraction import KeywordExtractionBase
from pipeline.pipeline import PipelineBase


class KeywordExtractionPipeline(PipelineBase):
    def __init__(self, keyword_extractor: KeywordExtractionBase):
        self.keyword_extractor = keyword_extractor

    def run(self, project: Project) -> Project:
        content = []
        for file in project.files:
            content.extend(file.identifiers)

        project.keywords = self.keyword_extractor.get_keywords(" ".join(content))

        return project
