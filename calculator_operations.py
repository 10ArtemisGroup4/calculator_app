class Color:
    purple = '\033[95m'
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'
    blue = '\033[94m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed. It is unidentified.")
        return a / b

class InteractiveCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.operations = {
            1: ("Addition", self.add),
            2: ("Subtraction", self.subtract),
            3: ("Multiplication", self.multiply),
            4: ("Division", self.divide),
        }


