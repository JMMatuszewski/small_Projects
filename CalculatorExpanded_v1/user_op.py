import time

from calculations import Calculations

class UserOp:
    def __init__(self):
        print("Init Menu")
        self.calc = Calculations()
        #self.options = (1,2,3,4)
        self.dict_opt = {
            "1" : self.calc.add,
            "2" : self.calc.subtract,
            "3" : self.calc.multiply,
            "4" : self.calc.divide
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
        """)

    def choice(self):
        choice = input('Choose action: ')
        if choice in self.dict_opt.keys():
            #print(f"You've chosen {choice}")
            val1, val2 = self._get_val()
            self.dict_opt[choice](val1,val2)
        else:
            print(f"Wrong command, proper commands are:\n-", "\n- ".join([str(option) for option in self.dict_opt.keys()]))

    def _get_val(self):
        #os.system('cls')
        self.val1 = int(input("1st value:"))
        self.val2 = int(input("2nd value:"))
        if self._check_data(self.val1) and self._check_data(self.val2):
            print("Wrong data - only numbers are acceptable")
        return self.val1, self.val2 #self.status

    def _check_data(self,val):
        if not type(val) == int:
            return  True
        return False