# 1935 후위 표기식2
def cal(n1, n2, oper):
    if oper == '+':
        return n2 + n1
    elif oper == '-':
        return n2 - n1
    elif oper == '*':
        return n2 * n1
    elif oper == '/':
        return n2 / n1

alphabet = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input())
formula = input()
op = ['+', '-', '*', '/']
stack = []
dic = dict()
for i in range(n):
    a = int(input())
    dic[alphabet[i]] = a

for element in formula:
    if element not in op:
        stack.append(dic[element])
    else:
        one = stack.pop()
        another = stack.pop()
        result = cal(one, another, element)
        stack.append(result)
print(f'{float(stack[-1]):.2f}')