def to_string(x, e):
    return str(x[0].eval(e))

def to_num(x, e):
    x = x[0].eval(e)
    return int(x)

def _input(*a):
    return input()

def _print(x, e):
    x = x[0].eval(e)
    print(x)

def _type(x, e):
    x = x[0].eval(e)
    if isinstance(x, str):
        return 'string'
    if isinstance(x, bool):
        return 'boolean'
    if isinstance(x, int):
        return 'num'
    return 'unknown'

def _exit(x, e):
    x = x[0].eval(e)
    import sys
    sys.exit(0)

