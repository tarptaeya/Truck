class If:
    def __init__(self):
        self.cond = None
        self.then = None
        self.otherwise = None

    def __repr__(self):
        return "If {cond} {then} Else {otherwise}".format(cond=self.cond, then=self.then, otherwise=self.otherwise)
