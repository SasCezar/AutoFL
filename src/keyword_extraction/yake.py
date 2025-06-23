from typing import List

from yake import yake

from keyword_extraction.keyword_extraction import KeywordExtractionBase


class YAKEKeywordExtraction(KeywordExtractionBase):
    """
    Class for keyword extraction using YAKE.
    """

    def __init__(self, stopwords_path=None, min_characters=3, **kwargs):
        super().__init__()
        self.stopwords = self.load_stopwords(stopwords_path)
        self.model = yake.KeywordExtractor(stopwords=self.stopwords, **kwargs)
        self.min_chars = min_characters

    def get_keywords(self, text: str) -> List[str]:
        """
        Returns the keywords of the text.
        :param text:
        :return:
        """
        return self.model.extract_keywords(text)

    @staticmethod
    def load_stopwords(path: str) -> List[str]:
        with open(path, "rt") as f:
            stopwords = f.read().splitlines()
        return stopwords
