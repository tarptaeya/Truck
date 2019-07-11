import reporter
import _globals as g

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

    def setup(self):
        self.set('str', g.to_string)
        self.set('num', g.to_num)
        self.set('input', g._input)
        self.set('print', g._print)
        self.set('println', g._println)
        self.set('type', g._type)
        self.set('exit', g._exit)

    def __repr__(self):
        r = f'{self.dict}'
        if self.parent:
            r += ' ' + self.parent.__repr__()
        return r

