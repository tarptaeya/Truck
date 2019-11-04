class Continue:
    def eval(self, _):
        raise ContinueException()

    def __repr__(self):
        return "Continue"


class ContinueException(Exception):
    def __init__(self):
        super().__init__()
