class Operations:

    def add(self, val1, val2):
        return val1 + val2

    def sub(self, val1, val2):
        return val1 - val2

    def mul(self, val1, val2):
        return val1 * val2

    def div(self, val1, val2):
        return val1 / val2

    def multi_oper(self,data_str):
        '''Calculate operation with multi basic operators'''
        out = 0
        num_state = False
        oper_state = False
        data_len = len(data_str)
        if data_len == 0:
            pass
        elif data_len == 1:
            out = data_str[0]
        else:
            out = data_str[0]
            for i, el in enumerate(data_str[1:],start=1):
                try:
                    if i%2 == 0:
                        num = el
                        num_state = True
                    else:
                        oper = el
                        oper_state = True

                    if num_state and oper_state:
                        if oper == '+':
                            out = self.add(out,num)
                        elif oper == '-':
                            out = self.sub(out,num)
                        elif oper == '*':
                            out = self.mul(out,num)
                        elif oper == '/':
                            out = self.div(out,num)
                        else:
                            print('Incorrect operator')
                            break
                        num_state = False
                        oper_state = False

                except Exception as e:
                    print(f"Error occurred: {e}")
                    break

        print(f'{str} = {out}')


