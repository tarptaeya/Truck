class Block:
    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        self.stmts.append(stmt)

    def eval(self, env):
        for stmt in self.stmts:
            stmt.eval(env)

    def __repr__(self):
        return "Block {}".format(self.stmts)
