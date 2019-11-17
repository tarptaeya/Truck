from .interpreter import *
from .interpreter.lexer import LexError
from .interpreter.parser import ParseError

__version__ = "0.1.1"
__about__ ="""Truck {version}
""".format(version=__version__)

def execute(string, env=None):
    if env is None:
        env = Environ()
    source = Source(string)
    lexer = Lexer(source)
    parser = Parser(lexer)
    node = parser.parse()
    return node.eval(env)


def run_file(path):
    with open(path) as f:
        execute(f.read())


def run_prompt():
    import readline
    print(__about__)
    count = 0
    env = Environ()

    def execute_line(cont=False):
        nonlocal line
        line += input(">>> " if not cont else "... ")
        source = Source(line)
        lexer = Lexer(source)
        parser = Parser(lexer)
        node = parser.parse()
        print("=> ".format(count), node.eval(env))

    while True:
        count += 1
        line = ""
        done = False
        cont = False
        while not done:
            try:
                execute_line(cont)
                done = True
            except (LexError, ParseError) as e:
                cont = True
                continue
            except KeyboardInterrupt:
                break
            except EOFError:
                return
            except Exception as e:
                print("  *", e)
                break
        print()
