class Lambda:
    def __init__(self):
        self.args = None
        self.body = None

    def __repr__(self):
        return "Lambda {args} {body}".format(args=self.args, body=self.body)
