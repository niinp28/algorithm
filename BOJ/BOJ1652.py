# 누울 자리를 찾아라

n = int(input())
arr = [list(input()) for _ in range(n)]
ans1 = 0
ans2 = 0
for i in range(n):
    tmp = 0
    tmp2 = 0
    for j in range(n):
        if arr[i][j] == '.':
            tmp += 1
            if tmp == 2:
                ans1 += 1
                
        if arr[i][j] == 'X':
            tmp = 0
        if arr[j][i] == '.':
            tmp2 += 1
            if tmp2 == 2:
                ans2 += 1
                
        if arr[j][i] == 'X':
            tmp2 = 0

print(ans1, ans2)