class Params:
    def __init__(self, *args):
        self.list = [*args]

    def add(self, expr):
        self.list.append(expr)

    def eval(self, env):
        ret = []
        for i in self.list:
            ret.append(i.eval(env))
        return ret

    def __repr__(self):
        return "Params {}".format(self.list)
