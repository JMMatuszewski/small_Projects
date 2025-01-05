import sys
import time
from ui import UI

class Calculator:
    def __init__(self):
        self.ui = UI()
        #self.status = True

    def run_calculator(self):
        print("Start calculator")
        while True:
            # if not self.status:
            #     sys.exit()
            self.ui.run_menu()

if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()