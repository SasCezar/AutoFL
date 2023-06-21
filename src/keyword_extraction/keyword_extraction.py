from abc import ABC


class KeywordExtractionBase(ABC):
    """
    Abstract class for keyword extraction

    """

    def __init__(self):
        self.model = None

    def get_keywords(self, text: str) -> List[str]:
        pass
