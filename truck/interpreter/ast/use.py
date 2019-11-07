import os

class Use:
    def __init__(self):
        self.path = []
        self.extern = False
        self.alias = None

    def eval(self, env):
        from ..environ import Environ
        from ..lexer import Lexer
        from ..parser import Parser
        from ..source import Source

        name = self.path[-1]
        if self.alias is not None:
            name = self.alias

        if self.path[0] == ".":
            pass # TODO: relative import
        elif self.extern:
            env.insert(name, __import__(".".join(self.path)))
        else:
            # import from std location
            path = "/".join(self.path) + ".truck"
            std_path = os.path.abspath(os.path.join(__file__, "../../../lib", path))
            e = Environ()
            with open(std_path) as f:
                p = Parser(Lexer(Source(f.read())))
                node = p.parse()
                node.eval(e)
            env.insert(name, e)

    def __repr__(self):
        return "Use {}".format(self.path)
