#
# bit1 = 0b0001
# bit2 = 0b0010
#
# a = 'aabbb'
# Data= [5.0, '+', '(', 11.0, '*', 500.0, ')', '/', '(', 22.0, '/', 5.0, ')', ')']
# print(Data.count(')'))

data0 = [1.0 , '+' , 2.0 , '*' , 3.0]
data01 = [1.0 , '+' , 2.0 , '*' , 3.0 , '-' , 4 ]
data_int = [1, '+', '(', 2, '*', '(' , 3 , '-' , 4 , ')' , ')' ]
data1 = [1.0, '+', '(', 2.0, '*', '(' , 3.0 , '-' , 4.0 , ')' , ')' ]
data2 = [1.0, '+', '(', 2.0, '*', '(' , 3.0 , '-' , 4.0 , ')' , '/', '(', 5.0, '+', 6.0, ')' , ')']
data3 = [1.0, '+', '(', 2.0, '*', 3.0 , ')' , '+' , 4.0 ]

# helpers
par = False
def solve(data):
    print(data)

    if '(' in data:
        print("go deeper")
        # for i, el in reversed(list(enumerate(data))):
        for i, el in enumerate(data):
            #print(f'el: {el}')
            if el == '(':
                #print(f'id: {i} of {el}')
                solve(data[i+1:])

        #return data
        print(f'END: {data}')
    # for i, el in enumerate(data):
    #     print(f'{i}: {el}')
    #     if par:

def oper(data):
    oper = ['*','/']

    if '*' in data or '/' in data:
        print("oper")

def slice(data):
    i = 3
    new_data = data[:i-1]
    new_data.append(6)
    new_data.extend(data[i+2:])

    print(data)
    print(new_data)

def short_list():
    lst = [1, '+' , 2 , '-' , 3 , '+' , 4]
    result = lst.pop(0)
    #print(result)
    for i, el in enumerate(lst):
        print(f'el: {el} | i: {i}')
        if el == '+':
            result += lst[i + 1]
        elif el == '-':
            result -= lst[i + 1]
        print(f'iter result: {result}')
    print(result)


def parenthesis(data_str):
    print(f'Data: {data_str}')
    # if len(data_str) > 1:
    if '(' in data_str or ')' in data_str:
        for i, el in enumerate(data_str):
            if el == '(':
                data_str = parenthesis(data_str[i+1:])
                print(f'ParData: {data_str}')
                break
    # elif ')' in data_str:
    #     for i, el in enumerate(data_str):
            elif el == ')':
                return data_str[:i]
            else:
                pass
    else:
        pass

    return data_str
    # else:
    #     result = data_str[0]
    #     return result


# solve(data1)
# oper(data0)
# slice(data01)
# short_list()

data = parenthesis(data1)
print(data)