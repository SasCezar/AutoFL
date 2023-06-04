from tree_sitter import Language

from entity.project import File
from parser.parser import AbstractParser


class ParserJava(AbstractParser):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. The parser is generated using antlr4.
    """
    def __init__(self):
        super().__init__()
        self.LANGUAGE = Language('/home/sasce/PycharmProjects/AutoFL/src/resources/languages.so', 'python')
        self.parser.set_language(self.LANGUAGE)

    def parse(self, file: File):
        code_b = bytes(file.content, "utf8")
        tree = self.parser.parse(code_b)
        return self._traverse(code_b, tree)
