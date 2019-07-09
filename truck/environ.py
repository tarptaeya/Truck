import reporter

class Environ:
    def __init__(self, parent=None):
        self.dict = {}
        self.parent = parent

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        if self.parent:
            return self.parent.get(key)
        return None

    def set(self, key, value):
        self.dict[key] = value

    def update(self, key, value):
        if key in self.dict:
            self.dict[key] = value
        elif self.parent:
            self.parent.update(key, value)
        else:
            reporter.report_error(f'unknown variable {key}')

