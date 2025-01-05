
class CheckData:

    def check_int(self, val):
        if not type(val) == int:
            return True
        return False

    def check_div(self,val):
        if val == 0:
            return True
        return False