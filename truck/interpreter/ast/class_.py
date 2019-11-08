from ..environ import Environ
from copy import deepcopy

class Class:
    def __init__(self):
        self.ident = None
        self.base = None
        self.methods = []

    def eval(self, env):
        self.env = env
        if self.ident is not None:
            env.insert(self.ident, self)
            return
        return self

    def __call__(self, *params):
        c = Class()
        c.ident = self.ident
        c.base = self.base
        c.methods = deepcopy(self.methods)

        def init_environ(x):
            base = self.env.get(x.base)
            if base is None:
                x.env = Environ(parent=self.env)
            else:
                init_environ(base)
                x.env = Environ(parent=base.env)
                x.env.insert("super", base)

            x.env.insert("this", x)
            for method in x.methods:
                method.eval(x.env)

        init_environ(c)

        constructor = c.env.get("constructor")
        if constructor is not None:
            constructor(*params)
        return c

    def __repr__(self):
        return "Class {} {}".format(self.ident, self.methods)

    def __getattr__(self, key):
        return self.env.get(key)
