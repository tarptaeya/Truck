class Args:
    def __init__(self):
        self.idents = []

    def add(self, ident):
        self.idents.append(ident)

    def __repr__(self):
        return "{}".format(self.idents)
