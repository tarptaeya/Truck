class Const:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "{}".format(self.value)


class Expr:
    def __init__(self, left=None, right=None, oper=None):
        self.left = left
        self.right = right
        self.oper = oper

    def __repr__(self):
        return "{left} {oper} {right}".format(left=self.left, oper=self.oper, right=self.right)
