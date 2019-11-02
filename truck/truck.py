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
    count = 0
    while True:
        count += 1
        try:
            line = input("In [{}]: ".format(count))
        except EOFError:
            break
        source = Source(line)
        lexer = Lexer(source)
        parser = Parser(lexer)
        node = parser.parse()
        print("Out[{}]:".format(count), node)
        print()

