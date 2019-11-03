class Source:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, index):
        if index >= len(self.string):
            return None

        return self.string[index]
