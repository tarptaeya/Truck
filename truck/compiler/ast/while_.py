class While:
    def __init__(self):
        self.cond = None
        self.block = None

    def __repr__(self):
        return "While {cond} {block}".format(cond=self.cond, block=self.block)
