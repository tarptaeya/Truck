class Decl:
    def __init__(self, ident=None, expr=None):
        self.ident = ident
        self.expr = expr

    def __repr__(self):
        return "Decl [{} = {}]".format(self.ident, self.expr)
