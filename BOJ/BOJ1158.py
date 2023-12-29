from collections import deque
N, K = map(int, input().split())
q = deque([x for x in range(1, N+1)])
ans = []
i = 0
while q:
    i += 1
    a = q.popleft()
    if not (i % K):
        ans.append(a)
        i = 0
    else:
        q.append(a)
print('<'+ ', '.join(map(str, ans)) + '>')
