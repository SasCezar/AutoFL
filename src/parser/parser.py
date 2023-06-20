from abc import ABC, abstractmethod
from antlr4 import InputStream, CommonTokenStream, Lexer, Parser
from entity.project import File
import logging
from parser.languages import register

logger = logging.getLogger(__name__)


class ParserBase(ABC):
    """
    Abstract class for a programming language parser.
    """

    def __init__(self):
        self.lexer: Lexer
        self.parser: Parser
        self.root = lambda x: x.compilationUnit()

    @abstractmethod
    def parse(self, file: File):
        """
        :param file:
        :return:
        """
        pass

    def _parse(self, text: str):
        input_stream = InputStream(text)
        lexer = self.lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.parser(stream)
        tree = self.root(parser)
        is_syntax_errors = tree.parser._syntaxErrors  # Binary
        return tree.toStringTree(recog=parser), is_syntax_errors

    def __init_subclass__(cls, lang: str):
        ParserFactory.register(lang, parser_class=cls)


class ParserFactory:
    """ The factory class for creating parsers"""

    registry = {}
    """ Internal registry for available parsers """

    @classmethod
    def register(cls, lang: str, parser_class: ParserBase):
        cls.registry[lang] = parser_class

    @classmethod
    def create_parser(cls, name: str, **kwargs) -> 'ParserBase':
        try:
            return cls.registry[name]()
        except KeyError:
            raise ValueError(f"Unknown parser : {name}")


# Keep here. Allows for the self register of the language specific parser in the language folder
register()
