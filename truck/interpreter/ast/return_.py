class Return:
    def __init__(self):
        self.expr = None

    def eval(self, env):
        value = self.expr.eval(env)
        raise ReturnException(value)

    def __repr__(self):
        return "Return {}".format(self.expr)


class ReturnException(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value
