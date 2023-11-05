# 괄호
N = int(input())
for _ in range(N):
    s = input()
    flag = 0
    if s[0] == ')' or s[-1] == '(':
        print('NO')
        continue
    else:
        for i in range(len(s)):
            if s[i] == '(':
                flag += 1
            else:
                flag -= 1
            
            if flag < 0:
                break
    if flag:
        print('NO')
    else:
        print('YES')