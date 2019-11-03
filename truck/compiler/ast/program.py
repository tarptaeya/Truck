class Program:
    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        self.stmts.append(stmt)

    def __repr__(self):
        return "Program {}".format(self.stmts)
