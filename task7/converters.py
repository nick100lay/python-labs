

from base_converter import BaseInputConverter


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
