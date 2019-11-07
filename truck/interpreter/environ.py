class Environ:
    def __init__(self, parent=None):
        self.env = {}
        self.parent = parent

    def get(self, item):
        if item in self.env:
            return self.env[item]
        if self.parent is not None:
            return self.parent.get(item)
        return None

    def insert(self, item, value):
        self.env[item] = value

    def update(self, item, value):
        curr = self
        while curr is not None:
            if item in curr.env:
                curr.env[item] = value
                return
            curr = curr.parent
        self.env[item] = value

    def __getattr__(self, item):
        # for example use io as IO, search only in self
        # and not in parent
        return self.env[item]

    def __repr__(self):
        rep = "{}".format(self.env)
        parent = self.parent
        while parent:
            rep += "\n" + parent.__repr__()
            parent = parent.parent
        return rep


class EnvironError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
