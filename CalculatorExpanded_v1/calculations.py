import os

class Calculations:

    def add(self,val1,val2):
        print("Adding...")
        out = val1 + val2
        print(f"{val1} + {val2} = {out}")
        input("Press to continue...")

    def subtract(self,val1,val2):
        print("Subtracting...")
        out = val1 - val2
        print(f"{val1} - {val2} = {out}")
        input("Press to continue...")

    def multiply(self,val1,val2):
        print("Multiplying...")
        out = val1 * val2
        print(f"{val1} * {val2} = {out}")
        input("Press to continue...")

    def divide(self,val1,val2):
        print("Dividing...")
        out = val1 / val2
        print(f"{val1} / {val2} = {out}")
        input("Press to continue...")


