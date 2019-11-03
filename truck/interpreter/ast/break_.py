class Break:
    def eval(self, _):
        raise BreakException()

    def __repr__(self):
        return "Break"


class BreakException(Exception):
    def __init__(self):
        super().__init__()
