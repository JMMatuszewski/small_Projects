import time

from calculations import Calculations
#from get_data import GetData

class UserOp:
    def __init__(self):
        print("Init Menu")
        self.calc = Calculations()
        #self.gd = GetData()
        #self.options = (1,2,3,4)
        self.dict_opt = {
            "1" : self.calc.add,
            "2" : self.calc.subtract,
            "3" : self.calc.multiply,
            "4" : self.calc.divide,

            "e" : self.calc.exit
        }

    def user_menu(self):
       # print("QRWA MAĆ CO JEST GRANE")
        print("""
        \n
        Options:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        ...
        e. Exit
        """)

    def choice(self):
        choice = input('Choose action: ')
        if choice in self.dict_opt.keys():
            # print(f"You've chosen {choice}")
            # val1, val2 = self.gd.get_val()
            self.dict_opt[choice]()
        else:
            print(f"Wrong command, proper commands are:\n-", "\n- ".join([str(option) for option in self.dict_opt.keys()]))
