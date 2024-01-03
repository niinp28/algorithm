n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
ans = []
num = 1
for i in range(len(target)):
    while True:
        if stack:
            if stack[-1] > target[i]:
                print('NO')
                exit()
            if stack[-1] == target[i]:
                stack.pop()
                ans.append('-')
                break
            else:
                stack.append(num)
                ans.append('+')
                num += 1
        else:
            stack.append(num)
            ans.append('+')
            num += 1

for e in ans:
    print(e)




'''
8
4
3
6
8
7
5
2
1
'''