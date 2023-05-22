from dataclasses import dataclass


@dataclass
class GitRankingLabel:
    def __int__(self):
        index: int
        label: str
        level: int
        kb_id: str


class GitRanking:
    def __int__(self, path):
        self.taxonomy = self.load()
        self.inverted = self.inverse()

    def load(self):
        pass

    def inverse(self):
        pass

    def __getitem__(self, item):
        return self.taxonomy[item]

    def get_label(self, index):
        return self.inverted[index]
