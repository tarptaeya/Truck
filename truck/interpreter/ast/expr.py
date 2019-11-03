class Const:
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value

    def __repr__(self):
        return "{}".format(self.value)


class Expr:
    def __init__(self, left=None, right=None, oper=None):
        self.left = left
        self.right = right
        self.oper = oper

    def eval(self, env):
        left = self.left.eval(env)
        right = self.right.eval(env)

        if self.oper == "or":
            return left or right
        if self.oper == "and":
            return left and right

        if self.oper == "==":
            return left == right
        if self.oper == "!=":
            return left != right

        if self.oper == "<=":
            return left <= right
        if self.oper == ">=":
            return left >= right
        if self.oper == "<":
            return left < right
        if self.oper == ">":
            return left > right

        if self.oper == "+":
            return left + right
        if self.oper == "-":
            return left - right
        if self.oper == "*":
            return left * right
        if self.oper == "/":
            return left / right
        if self.oper == "%":
            return left % right

        if self.oper == "|":
            return left | right
        if self.oper == "&":
            return left & right

        if self.oper == "()":
            return left(*right)

    def __repr__(self):
        return "{left} {oper} {right}".format(left=self.left, oper=self.oper, right=self.right)
