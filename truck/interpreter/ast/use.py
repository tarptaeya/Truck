class Use:
    def __init__(self):
        self.path = []
        self.alias = None

    def eval(self, env):
        pass

    def __repr__(self):
        return "Use {}".format(self.path)
