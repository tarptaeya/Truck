class Params:
    def __init__(self, *args):
        self.list = [*args]

    def add(self, expr):
        self.list.append(expr)

    def __repr__(self):
        return "Params {}".format(self.list)
