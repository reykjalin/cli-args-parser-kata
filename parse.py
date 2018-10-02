class ArgumentParser:
    def __init__(self, args):
        if isinstance(args, str):
            args = args.split(" ")
        self.args = args[1:]

    def parse(self):
        args_dict = {}
        key = ""

        while len(self.args) > 0:
            if len(self.args) == 1 or self.args[1].startswith("--"):
                args_dict.update(self.parse_simple(self.args[0]))
            else:
                args_dict.update(self.parse_composite(self.args[0 : 2]))
                self.args.remove(self.args[1])
            self.args.remove(self.args[0])

        return args_dict

    def parse_simple(self, arg):
        return {arg[2:]: True}

    def parse_composite(self, arg):
        flag = arg[0][2:]
        value = arg[1]
        try:
            return {flag: int(value)}
        except:
            return {flag: value}
