import re

from entity.project import File
from grammars.python3.Python3Lexer import Python3Lexer
from grammars.python3.Python3Parser import Python3Parser

from parser.parser import ParserBase


class ParserPython3(ParserBase, lang='python3'):
    """
    Python code parser. The lexer and parser have been generated using a version agnostic python grammar for antlr4.
    """

    def __init__(self, remap_alias=False):
        super().__init__()
        self.lexer = Python3Lexer
        self.parser = Python3Parser
        self.alias = re.compile(r"\(dotted_as_name \(dotted_name (?:<name>\w*)\) as (?:<alias>\w*)\)")
        self.identifiers_re = re.compile(r"(?:atom|trailer \.|import_as_name|as|class|funcdef def|tfpdef) (\w*)|(?:dotted_name) (\w*)(?: \. )?(\w*)?")
        self.root = lambda x: x.file_input()

    def parse(self, file: File):
        content = file.content
        alias_map = {m.groupdict() for m in self.alias.finditer(content)}
        ast = self._parse(file.content)
        print(ast)
        # Flatten list and remove empty tokens
        identifiers = [x for x in sum(self.identifiers_re.findall(str(ast)), ()) if x]

        return identifiers
