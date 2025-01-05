from calculations import Calculations

class UserOp:
    def __init__(self):
        print("Init Menu")
        self.calc = Calculations()
        self.dict_opt = {
            "1" : self.calc.add,
            "2" : self.calc.subtract,
            "3" : self.calc.multiply,
            "4" : self.calc.divide,
            "5" : self.calc.basic_calcs,

            "e" : self.calc.exit
        }

    def user_menu(self):
        print("""
        \n
        Options:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Basic Calculations (+ - * /)
        ...
        e. Exit
        """)

    def choice(self):
        choice = input('Choose action: ')
        if choice in self.dict_opt.keys():
            self.dict_opt[choice]()
        else:
            print(f"Wrong command, proper commands are:\n-", "\n- ".join([str(option) for option in self.dict_opt.keys()]))
