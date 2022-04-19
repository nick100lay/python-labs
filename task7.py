

import math
import random


operators = {}
def register_operator(op):
    operators[op.name] = op


def show_usage():
    for op in operators.values():
        op.show_help()


def input_operator():
    op_name = input("Write operator: ")
    if op_name not in operators:
        print("Invalid operator")
        exit()
    return operators[op_name]


def execute_operator(op):
    try:
        print("Result:", op.execute())
    except (ArithmeticError, ValueError):
        print("Arithmetic error")
        exit()


class BaseInputConverter:
    def convert(self, line):
        pass

    def get_name(self):
        pass


class AnyNumTypeInputConverter(BaseInputConverter):
    def convert(self, line):
        try:
            return int(line)
        except ValueError:
            pass
        return float(line)

    def get_name(self):
        return "any number type"


class IntegerInputConverter(BaseInputConverter):
    def convert(self, line):
        return int(line)

    def get_name(self):
        return "integer"


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
            args.append(arg.convert(input(msg)))

        return self.execute_func(*args)

    def execute_func(self, *args):
        return type(self).func(*args)

    def show_help_desc(self):
        return self.desc

    def get_args(self):
        return self.args

    def get_name(self):
        return self.name


class AddOperator(OperatorWithArgs):
    name = "+"
    desc = "Add two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x + y
register_operator(AddOperator())

class SubOperator(OperatorWithArgs):
    name = "-"
    desc = "Subtract two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x - y
register_operator(SubOperator())

class MulOperator(OperatorWithArgs):
    name = "*"
    desc = "Multiply two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x * y
register_operator(MulOperator())

class DivOperator(OperatorWithArgs):
    name = "/"
    desc = "Divide two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x / y
register_operator(DivOperator())

class PowOperator(OperatorWithArgs):
    name = "pow"
    desc = "a power of b"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x ** y
register_operator(PowOperator())

class AbsOperator(OperatorWithArgs):
    name = "abs"
    desc = "Absolute number value"
    args = (AnyNumTypeInputConverter(),)
    func = abs
register_operator(AbsOperator())

class RandOperator(OperatorWithArgs):
    name = "rand"
    desc = "Random number"
    args = ()
    func = random.random
register_operator(RandOperator())

class FactorialOperator(OperatorWithArgs):
    name = "factorial"
    desc = "Factorial of number"
    args = (IntegerInputConverter(),)
    func = math.factorial
register_operator(FactorialOperator())

class AcosOperator(OperatorWithArgs):
    name = "acos"
    desc = "Arccos of number"
    args = (AnyNumTypeInputConverter(),)
    func = math.acos
register_operator(AcosOperator())


show_usage()
print()
execute_operator(input_operator())
