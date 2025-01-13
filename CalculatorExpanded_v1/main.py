from ui import UI

class Calculator:
    def __init__(self):
        self.ui = UI()

    def run_calculator(self):
        print("Start calculator")
        while True:
            self.ui.run_menu()

if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()