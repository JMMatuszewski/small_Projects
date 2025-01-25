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

        # 2 + 5 * 2 - (5 / 2)


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

    def parenthesis(self,data_str):
        if '(' in data_str:
            for i, el in enumerate(data_str):
                if el == '(':
                    return self.pemdas(data_str[i + 1:])
        else:
            for i,el in enumerate(data_str):
                if el == ')':
                    return data_str[:i]


    def order(self,data_str):
        '''Transform data by calculations with orded of operations'''
        out = []
        skip = False
        skip_count = 1
        for i,el in enumerate(data_str):
            if skip:
                skip_count += 2
                skip = False
                continue

            if el == '*':
                result = self.mul(out[i-1],data_str[i+1])
                out[i-1] = result
                skip = True

            elif el == '/':
                result = self.div(out[i - 1], data_str[i + 1])
                out[i-1] = result
                skip = True
            else:
                out.append(el)
        return out

    def count_str(self,data_str):

        result = data_str[0]
        for i, el in enumerate(data_str):
            if el == '+':
                result += data_str[i + 1]
            elif el == '-':
                result -= data_str[i + 1]
        return result


    def pemdas(self,data):
        if '(' in data:
            for i, el in enumerate(data):
                if el == '(':
                    return self.pemdas(data[i+1:])
        for i,el in enumerate(data):
            if el == ')'

        # if '*' in data or '/' in data:
        #     for i, el in enumerate(data):
        #         if el == '*':
        #             result = self.mul(data[i-1],data[i+1])
        #             new_data = data[:i - 1]
        #             new_data.append(result)
        #             new_data.extend(data[i + 2:])
        #             data = new_data
