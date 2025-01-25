import sys

from calculations import Operations
from get_data import GetData
from check_tools import CheckData

class Calculations:

    def __init__(self):
        self.op = Operations()
        self.gd = GetData()
        self.cd = CheckData()

    def add(self):
        print('Input numbers, finish with "="')
        data = self.gd.get_val()
        val_end = len(data)
        if val_end == 0:
            out = 0
        elif val_end == 1:
            out = data[0]
            print(f"{out}", end='')
        else:
            out = data[0]
            print(f"{out}", end='')
            for i in range(1,val_end):
                out = self.op.add(out,data[i])
                print(f' + {data[i]}', end='')
        print(f" = {out}")

    def subtract(self):
        print('Input numbers, finish with "="')
        data = self.gd.get_val()
        val_end = len(data)
        if val_end == 0:
            out = 0
        elif val_end == 1:
            out = data[0]
            print(f"{out}", end='')
        else:
            out = data[0]
            print(f"{out}", end='')
            for i in range(1,val_end):
                out = self.op.sub(out,data[i])
                print(f' - {data[i]}', end='')
        print(f" = {out}")

    def multiply(self):
        print('Input numbers, finish with "="')
        data = self.gd.get_val()
        val_end = len(data)
        if val_end == 0:
            out = 0
        elif val_end == 1:
            out = data[0]
            print(f"{out}", end='')
        else:
            out = data[0]
            print(f"{out}", end='')
            for i in range(1,val_end):
                out = self.op.mul(out,data[i])
                print(f' * {data[i]}', end='')
        print(f" = {out}")

    def divide(self):
        print('Input numbers, finish with "="')
        data = self.gd.get_val(True)
        val_end = len(data)
        if val_end == 0:
            out = 0
        elif val_end == 1:
            out = data[0]
            print(f"{out}", end='')
        else:
            out = data[0]
            print(f"{out}", end='')
            for i in range(1,val_end):
                out = self.op.div(out,data[i])
                print(f' / {data[i]}', end='')
        print(f" = {out}")

    def basic_calcs(self):
        '''Calculations without order of operations'''
        print("Create number-operator operation")
        data_str = self.gd.get_str_val()
        print(f'Data: {data_str}')
        #self.op.multi_oper(data_str)
        self.op.pemdas(data_str)



    def exit(self):
        sys.exit()

