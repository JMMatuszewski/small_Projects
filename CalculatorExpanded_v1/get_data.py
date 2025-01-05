from check_data import CheckData

class GetData:
    def __init__(self):
        self.cd = CheckData()

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

