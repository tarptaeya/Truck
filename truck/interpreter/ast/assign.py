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

        # when you assign to an attrib, then insert it to
        # the env of attrib
        #
        # x = "hello"
        # class A { constructor() { this.x = 4 } }
        #
        # now here x must remain "hello" and not 4
        left = self.lvalue.left.eval(env)
        left.env.insert(self.lvalue.right.value, self.rvalue.eval(env))

    def __repr__(self):
        return "Assign [{} = {}]".format(self.lvalue, self.rvalue)
