class ArgumentParser:
    def __init__(self, args):
        self.args = args[1:]

    def parse(self):
        args_dict = {}
        key = ""

        for arg in self.args:
            if arg.startswith("--"):
                key = arg[2:]
                args_dict[key] = ""
            else:
                args_dict[key] = arg

        return args_dict
