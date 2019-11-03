from .interpreter import *

__version__ = "0.1.0"
__about__ ="""Truck {version}
""".format(version=__version__)

def execute(string, env=Environ()):
    source = Source(string)
    lexer = Lexer(source)
    parser = Parser(lexer)
    node = parser.parse()
    return node.eval(env)


def run_file(path):
    pass


def run_prompt():
    import readline
    print(__about__)
    count = 0
    env = Environ()
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
        print("Out[{}]:".format(count), node.eval(env))
        print()

