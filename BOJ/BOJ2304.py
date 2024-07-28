# 창고 다각형
n = int(input())
storage = [tuple(map(int, input().split())) for _ in range(n)]
storage.sort()

lst = [0] * 1001
ans = 0
start = storage[0][0]
end = storage[-1][0]

mxh = 0
idx = 0
for L in storage:
    lst[L[0]] = L[1]
    if L[1] > mxh:
        mxh = L[1]
        idx = L[0]

cur = 0
for i in range(start, end+1):
    if i == idx:
        cur = max(cur, lst[i])
        ans += cur
        break
    cur = max(cur, lst[i])
    ans += cur
        
cur = 0
for i in range(end, start-1, -1):
    if i == idx:
        break
    cur = max(cur, lst[i])
    ans += cur
print(ans)
'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''