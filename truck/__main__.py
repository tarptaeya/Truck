import sys
from .truck import *

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        run_prompt()
    else:
        run_file(args[0])
