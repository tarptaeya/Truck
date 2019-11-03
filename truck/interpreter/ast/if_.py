class If:
    def __init__(self):
        self.cond = None
        self.then = None
        self.otherwise = None

    def eval(self, env):
        cond = self.cond.eval(env)
        if cond:
            self.then.eval(env)
        elif self.otherwise is not None:
            self.otherwise.eval(env)
        return None

    def __repr__(self):
        return "If {cond} {then} Else {otherwise}".format(cond=self.cond, then=self.then, otherwise=self.otherwise)
