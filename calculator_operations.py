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
    def display_menu(self):
        print(f"\n{Color.cyan}{'='*30}{Color.end}")
        print(f"{Color.yellow}{Color.bold} Calculator Menu{Color.end}")
        print(f"{Color.cyan}{'='*30}{Color.end}")
        for key, (name, _) in self.operations.items():
            print(f"{Color.green}{key}.{Color.end} {name}")
        print(f"{Color.cyan}{'='*30}{Color.end}")

    def get_operation_choice(self):
        while True:
            try:
                choice = int(input(f"{Color.blue}Choose an operation (1-4): {Color.end}"))
                if choice in self.operations:
                    return choice
                else:
                    print(f"{Color.red}Invalid choice. Please enter a number between 1 and 4{Color.end}")
            except ValueError:
                print(f"{Color.red}Invalid input. Please enter a number.{Color.end}")

    def get_two_numbers(self):
        while True:
            try:
                num1 = float(input(f"{Color.blue}Enter first number: {Color.end}"))
                num2 = float(input(f"{Color.yellow}Enter second number: {Color.end}"))
                return num1, num2
            except ValueError:
                print(f"{Color.red}Invalid input. Please enter a numeric value (e.g., 5, 3.2).{Color.end}")

    def ask_to_continue(self):
        answer = input(f"\n{Color.yellow}Do you want to continue? (y/n): {Color.end}").strip().lower()
        return answer in ("y")

    

