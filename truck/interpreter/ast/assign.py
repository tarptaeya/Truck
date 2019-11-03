from .ident import Ident
from .expr import Expr

class Assign:
    def __init__(self, lvalue=None, rvalue=None):
        self.lvalue = lvalue
        self.rvalue = rvalue

    def eval(self, env):
        if isinstance(self.lvalue, Ident):
            env.update(self.lvalue.value, self.rvalue.eval(env))
            return

        # "." oper
        if self.lvalue.oper != ".":
            raise Exception # TODO: unsupported assignment
        left = self.lvalue.left.eval(env)
        left.env.update(self.lvalue.right.value, self.rvalue.eval(env))

    def __repr__(self):
        return "Assign [{} = {}]".format(self.lvalue, self.rvalue)
