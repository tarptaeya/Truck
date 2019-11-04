class While:
    def __init__(self):
        self.cond = None
        self.block = None

    def eval(self, env):
        while self.cond.eval(env):
            self.block.eval(env)

    def __repr__(self):
        return "While {cond} {block}".format(cond=self.cond, block=self.block)
