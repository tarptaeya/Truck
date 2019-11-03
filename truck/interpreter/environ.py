class Environ:
    def __init__(self, env={}, parent=None):
        self.env = env
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
        if item in self.env:
            self.env[item] = value
        elif self.parent is not None:
            self.parent.update(ident, value)
        else:
            raise EnvironError("{} not found in environ".format(ident))


class EnvironError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
