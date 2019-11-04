from .return_ import ReturnException
from ..environ import Environ

class Function:
    def __init__(self):
        self.ident = None
        self.args = None
        self.body = None

    def eval(self, env):
        self.env = env
        if self.ident is not None:
            env.insert(self.ident, self)
            return
        return self

    def __call__(self, *params):
        assert(len(self.args) == len(params))
        env = Environ(parent=self.env)
        for (k, v) in zip(self.args, params):
            env.insert(k, v)
        try:
            self.body.eval(env)
        except ReturnException as R:
            return R.value

    def __repr__(self):
        if self.ident:
            return "Function {ident} {args} {body}".format(ident=self.ident, args=self.args, body=self.body)
        return "Function {args} {body}".format(args=self.args, body=self.body)
