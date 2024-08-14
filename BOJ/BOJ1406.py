# 에디터

word = input()
n = int(input())
leftstack = list(word)
rightstack = []
for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        if leftstack:
            rightstack.append(leftstack.pop())
    elif command[0] == 'D':
        if rightstack:
            leftstack.append(rightstack.pop())
    elif command[0] == 'B':
        if leftstack:
            leftstack.pop()
    elif command[0] == 'P':
        leftstack.append(command[1])
print(''.join(map(str, (leftstack + rightstack[::-1]))))