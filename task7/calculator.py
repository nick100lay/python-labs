

class Calculator:

    def __init__(self):
        self.operators = {}

    def register_operators(self, *operators):
        for op in operators:
            self.operators[op.get_name()] = op

    def show_usage(self):
        for op in self.operators.values():
            op.show_help()

    def has_operator(self, op_name):
        return op_name in self.operators

    def execute_operator(self, op_name):
        return self.operators[op_name].execute()
