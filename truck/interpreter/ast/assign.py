class Assign:
    def __init__(self, ident=None, expr=None):
        self.ident = ident
        self.expr = expr

    def eval(self, env):
        env.update(self.ident, self.expr.eval(env))

    def __repr__(self):
        return "Assign [{} = {}]".format(self.ident, self.expr)
