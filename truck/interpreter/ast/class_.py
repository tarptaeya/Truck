from ..environ import Environ
from copy import deepcopy

class Class:
    def __init__(self):
        self.ident = None
        self.base = None
        self.methods = []

    def eval(self, env):
        base = env.get(self.base)
        if base is None:
            self.env = Environ(parent=env)
        else:
            self.env = Environ(parent=base.env)
            self.env.insert("super", base.env.get("this"))

        self.env.insert("this", self)

        for method in self.methods:
            method.eval(self.env)
        env.insert(self.ident, self)
        return self

    def __call__(self, *params):
        constructor = self.env.get("constructor")
        if constructor is not None:
            constructor(*params)
        return deepcopy(self)

    def __repr__(self):
        return "Class {}".format(self.methods)
