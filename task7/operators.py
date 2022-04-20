

import math
import random


from base_operator import OperatorWithArgs
from converters import AnyNumTypeInputConverter, IntegerInputConverter


class AddOperator(OperatorWithArgs):
    name = "+"
    desc = "Add two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x + y


class SubOperator(OperatorWithArgs):
    name = "-"
    desc = "Subtract two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x - y


class MulOperator(OperatorWithArgs):
    name = "*"
    desc = "Multiply two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x * y


class DivOperator(OperatorWithArgs):
    name = "/"
    desc = "Divide two numbers"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x / y


class PowOperator(OperatorWithArgs):
    name = "pow"
    desc = "a power of b"
    args = (AnyNumTypeInputConverter(),
            AnyNumTypeInputConverter())
    func = lambda x, y: x ** y


class AbsOperator(OperatorWithArgs):
    name = "abs"
    desc = "Absolute number value"
    args = (AnyNumTypeInputConverter(),)
    func = abs


class RandOperator(OperatorWithArgs):
    name = "rand"
    desc = "Random number"
    args = ()
    func = random.random


class FactorialOperator(OperatorWithArgs):
    name = "factorial"
    desc = "Factorial of number"
    args = (IntegerInputConverter(),)
    func = math.factorial


class AcosOperator(OperatorWithArgs):
    name = "acos"
    desc = "Arccos of number"
    args = (AnyNumTypeInputConverter(),)
    func = math.acos
