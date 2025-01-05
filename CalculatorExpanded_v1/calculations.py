import os
import sys
from get_data import GetData
from check_data import CheckData

class Calculations:

    def __init__(self):
        self.gd = GetData()
        self.cd = CheckData()

    def add(self):
        print("Adding...")
        val1, val2 = self.gd.get_val()
        out = val1 + val2
        print(f"{val1} + {val2} = {out}")
        input("Press to continue...")

    def subtract(self):
        print("Subtracting...")
        val1, val2 = self.gd.get_val()
        out = val1 + val2
        print(f"{val1} - {val2} = {out}")
        input("Press to continue...")

    def multiply(self):
        print("Multiplying...")
        val1, val2 = self.gd.get_val()
        out = val1 * val2
        print(f"{val1} * {val2} = {out}")
        input("Press to continue...")

    def divide(self):
        print("Dividing...")
        val1, val2 = self.gd.get_val()
        if self.cd.check_div(val2):
            print("2nd value cannot be 0")
            input("Press to continue...")
            return
        out = val1 / val2
        print(f"{val1} / {val2} = {out}")
        input("Press to continue...")

    def exit(self):
        sys.exit()

