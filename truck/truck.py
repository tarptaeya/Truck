from .compiler import Lexer
from .compiler import Parser
from .compiler import Source

__version__ = "0.1.0"
__about__ ="""Truck {version}
""".format(version=__version__)

def execute(string):
    pass


def run_file(path):
    pass


def run_prompt():
    import readline
    print(__about__)
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break
        source = Source(line)
        lexer = Lexer(source)
        parser = Parser(lexer)
        node = parser.parse()
        print(node)

