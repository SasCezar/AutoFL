from entity.project import File
from parser.parser import AbstractParser


class ParserJava(AbstractParser):
    """
    Java specific parser. Uses a generic grammar for multiple versions of java. The parser is generated using antlr4.
    """
    def __init__(self):
        super().__init__()


    def parse(self, file: File):
        pass
