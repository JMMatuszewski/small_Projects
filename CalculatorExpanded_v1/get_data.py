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
        opers = ['+','-','*','/']
        # 0b1010 | num-oper-(-)
        next_aval = 10
        brackets = 0
        data = []
        str = ''

        while True:
            print('\n'*10)
            val = input(f'>{str} ')
            if val == '=':
                if brackets != 0:
                    print("Close all the brackets")
                    continue
                else:
                    return data

            # Check for number
            if next_aval & (1 << 3):
                try:
                    fval = float(val)
                    data.append(fval)
                    str += val
                    next_aval = 0b0101 #5
                    continue
                except ValueError:
                    pass

            # Check for operator
            if next_aval & (1 << 2):
                if val in opers:
                    data.append(val)
                    str += val
                    next_aval = 0b1010 #10
                    continue

            # Check for ' ( '
            if next_aval & (1 << 1):
                if val == '(':
                    data.append(val)
                    str += val
                    next_aval = 0b1010 #10
                    brackets += 1
                    continue

            # Check for ' ) '
            if next_aval& (1 << 0):
                if val == ')' and brackets > 0:
                    data.append(val)
                    str += val
                    next_aval = 0b0101 #5
                    brackets -= 1
                    continue
