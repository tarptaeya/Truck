import os

class Use:
    def __init__(self):
        self.path = []
        self.alias = None

    def eval(self, env):
        from ..lexer import Lexer
        from ..parser import Parser
        from ..source import Source
        if self.path[0] == ".":
            pass # TODO: relative import
        else:
            # import from std location
            path = "/".join(self.path) + ".truck"
            std_path = os.path.abspath(os.path.join(__file__, "../../../lib", path))
            with open(std_path) as f:
                p = Parser(Lexer(Source(f.read())))
                node = p.parse()
                node.eval(env)

    def __repr__(self):
        return "Use {}".format(self.path)
