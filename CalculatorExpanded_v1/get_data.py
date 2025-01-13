import os
from check_tools import CheckData

class GetData:
    def __init__(self):
        self.cd = CheckData()
        self.opers = ['+','-','*','/']

    def get_val(self,div=False):
        '''Get any number of inputs, flag div=True for divisor check'''
        data = []
        while True:
            try:
                val = input(f'{len(data)+1}{self.cd.ord_nums(len(data)+1)} value:')
                if val == '=':
                    return data
                val_int = float(val)
                if div and val_int == 0:
                    print("Divisor cannot be 0")
                    continue
                data.append(val_int)
            except ValueError:
                print("Wrong data - only numbers are acceptable")

    def get_str_val(self):
        '''Create string made of numbers and basic operators'''
        data = []
        str = '>'
        num_oper = 1
        while True:
            try:
                # val = input(f"{'num :' if num_oper%2 != 0 else 'oper:'}")
                print('\n'*20)
                val = input(f'{str} ')
                if val == '=':
                    return data

                if num_oper%2 != 0:
                    fval = float(val)
                    if len(data) > 2:
                        if data[-1] == '/' and fval == 0:
                            print("Divisor cannot be 0")
                            continue
                    data.append(fval)
                    str += val
                    num_oper += 1
                    print(data)
                else:
                    if val not in self.opers:
                        print("Wrong operator")
                        continue
                    data.append(val)
                    str += val
                    num_oper += 1
                    print(data)

            except ValueError:
                print("Wrong data - only numbers are acceptable")