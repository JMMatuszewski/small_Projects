from check_data import CheckData

class GetData:
    def __init__(self):
        self.cd = CheckData()

    def get_val(self):
        # os.system('cls')
        # print("Getting data...")
        val1 = int(input("1st value:"))
        val2 = int(input("2nd value:"))
        if self.cd.check_int(val1) and self.cd.check_int(val2):
            print("Wrong data - only numbers are acceptable")
        return val1, val2  # self.status

