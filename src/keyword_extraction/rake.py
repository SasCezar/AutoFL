from typing import List

from RAKE import Rake

from keyword_extraction.keyword_extraction import KeywordExtractionBase


class RAKEKeywordExtraction(KeywordExtractionBase):
    """
    Class for keyword extraction using RAKE.
    """

    def __init__(self, stopwords_path=None, **kwargs):
        super().__init__()
        self.model = Rake(stopwords_path)
        self.kwargs = kwargs

    def get_keywords(self, text: str) -> List[str]:
        """
        Returns the keywords of the text.
        :param text:
        :return:
        """
        return self.model.run(text, **self.kwargs)
