class Ident:
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return env.get(self.value)

    def __repr__(self):
        return "Ident [{}]".format(self.value)
