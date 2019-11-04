class Program:
    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        self.stmts.append(stmt)

    def eval(self, env):
        ret = 0
        for stmt in self.stmts:
            ret = stmt.eval(env)
        return ret

    def __repr__(self):
        return "Program {}".format(self.stmts)
