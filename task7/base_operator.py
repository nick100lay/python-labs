

class InvalidArgumentError(Exception):
    pass


class BaseOperator:
    def show_help(self):
        pass

    def execute(self):
        pass


class OperatorWithArgs(BaseOperator):
    def show_help(self):
        print(self.get_name(), len(self.get_args()), "arguments",
                "(", ", ".join(
                    map(lambda arg: arg.get_name(),
                        self.get_args())), ").",
                    self.show_help_desc())

    def execute(self):
        args = []

        for i, arg in enumerate(self.get_args()):
            msg = "%i. Write %s argument: " % (i + 1, arg.get_name())
            try:
                args.append(arg.convert(input(msg)))
            except ValueError:
                raise InvalidArgumentError()

        return self.execute_func(*args)

    def execute_func(self, *args):
        return type(self).func(*args)

    def show_help_desc(self):
        return self.desc

    def get_args(self):
        return self.args

    def get_name(self):
        return self.name
