import os
import sys
import reporter

from environ import Environ
from source import Source
from lexer import Lexer
from parser import Parser

def init_environ(filename=None):
    if not filename:
        dirname = os.getcwd()
    else:
        dirname = os.path.dirname(filename)
    environ = Environ()
    environ.set('__dir__', dirname)
    return environ

def run_prompt():
    environ = init_environ()
    environ.setup()
    reporter.abort_on_error = False
    print('Truck v0.1\n')
    while True:
        try:
            string = input('>>> ')
            source = Source(string)
            lexer = Lexer(source)
            parser = Parser(lexer)
            parser.parse()
            try:
                parser.root.debug = True
                parser.root.eval(environ)
            except Exception as e:
                print(f'{e}')
        except (KeyboardInterrupt, EOFError):
            print('Bye!')
            sys.exit(0)


def run_file(filename):
    string = ''
    with open(filename, 'r') as f:
        string += f.read()
    source = Source(string)
    lexer = Lexer(source)
    parser = Parser(lexer)
    parser.parse()
    environ = init_environ(filename)
    environ.setup()
    parser.root.eval(environ)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[-1]
        run_file(filename)
    elif len(sys.argv) == 1:
        run_prompt()
    else:
        print('error')

