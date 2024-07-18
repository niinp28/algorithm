# 크게 만들기

N, K = map(int, input().split())
number = list(map(int, input()))
stack = []

for num in number:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    print(''.join(map(str, stack[:-K])))
else:
    print(''.join(map(str, stack)))