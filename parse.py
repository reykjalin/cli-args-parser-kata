class ArgumentParser:
    def __init__(self, args):
        self.args = args[1:]

    def parse(self):
        args_dict = {}
        key = ""

        for arg in self.args:
            args_dict[arg[2:]] = True

        return args_dict

    def parse_simple(self, arg):
        return {arg[2:]: True}

    def parse_composite(self, arg):
        return {arg[0][2:]: arg[1]}
