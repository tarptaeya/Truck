class Decl:
    def __init__(self, ident=None, expr=None):
        self.ident = ident
        self.expr = expr

    def eval(self, env):
        env.insert(self.ident, self.expr.eval(env))

    def __repr__(self):
        return "Decl [{} = {}]".format(self.ident, self.expr)
