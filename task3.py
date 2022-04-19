

import math
import random


def any_num_type(s):
    try:
        return int(s)
    except ValueError:
        pass
    return float(s)



operators = {
        "+": (lambda x, y: x + y, (any_num_type, any_num_type)),
        "-": (lambda x, y: x - y, (any_num_type, any_num_type)),
        "/": (lambda x, y: x / y, (any_num_type, any_num_type)),
        "*": (lambda x, y: x * y, (any_num_type, any_num_type)),
        "pow": (lambda x, y: x ** y, (any_num_type, any_num_type)),
        "abs": (abs, (any_num_type,)),
        "rand": (random.random, ()),
        "factorial": (math.factorial, (int,)),
        "acos": (math.acos, (float,)),
        }


print("Usage")
print("Operators:")

for op_name, op in operators.items():
    print(op_name, len(op[1]), "arguments",
            "(", ", ".join(map(lambda arg: arg.__name__, op[1])), ")")


print()

op_name = input("Write operator: ")
if op_name not in operators:
    print("Invalid operator")
    exit()


op = operators[op_name]
args = []

for i, arg in enumerate(op[1]):
    try:
        msg = "%i. Write %s argument: " % (i + 1, arg.__name__)
        args.append(arg(input(msg)))
    except ValueError:
        print("Wrong argument")
        exit()

try:
    print("Result:", op[0](*args))
except (ArithmeticError, ValueError):
    print("Arithmetic error")


