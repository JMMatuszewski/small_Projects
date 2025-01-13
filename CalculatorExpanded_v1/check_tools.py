
class CheckData:

    # def check_int(self, val):
    #     if not type(val) == int:
    #         return True
    #     return False

    def ord_nums(self,val):
        '''Ordinal numbers given depending on input value'''
        if val == 1:
            return 'st'
        if val == 2:
            return 'nd'
        if val == 3:
            return 'rd'
        else:
            return 'th'

    def check_div(self,val):
        if val == 0:
            return True
        return False

