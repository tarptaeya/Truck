class New:
    def __init__(self, obj=None):
        self.object = obj

    def eval(self, env):
        return env

    def __repr__(self):
        return "New {}".format(self.object)
