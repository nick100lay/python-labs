

from base_operator import InvalidArgumentError
from calculator import Calculator
import operators


def execute_operator(calc, op_name):
    if not calc.has_operator(op_name):
        print("Invalid operator")
        exit()

    try:
        print("Result:", calc.execute_operator(op_name))
    except InvalidArgumentError:
        print("Invalid argument")
        exit()
    except (ArithmeticError, ValueError):
        print("Arithmetic error")
        exit()


calc = Calculator()
calc.register_operators(
        operators.AddOperator(),
        operators.SubOperator(),
        operators.DivOperator(),
        operators.MulOperator(),
        operators.PowOperator(),
        operators.AbsOperator(),
        operators.RandOperator(),
        operators.FactorialOperator(),
        operators.AcosOperator(),
        )
calc.show_usage()
print()
execute_operator(calc, input("Write operator: "))
