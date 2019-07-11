import sys
import reporter

from environ import Environ
from source import Source
from lexer import Lexer
from parser import Parser

def run_prompt():
    environ = Environ()
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


def run_file(filenames):
    string = ''
    for filename in filenames:
        with open(filename, 'r') as f:
            string += f.read()
    source = Source(string)
    lexer = Lexer(source)
    parser = Parser(lexer)
    parser.parse()
    environ = Environ()
    environ.setup()
    parser.root.eval(environ)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1:]
        run_file(filename)
    elif len(sys.argv) == 1:
        run_prompt()

