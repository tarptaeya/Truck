class Assign:
    def __init__(self, ident=None, expr=None):
        self.ident = ident
        self.expr = expr

    def __repr__(self):
        return "Assign [{} = {}]".format(self.ident, self.expr)
