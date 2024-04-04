# 프린터 큐
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    ans = 1
    while q:
        a = q[0]
        if a < max(q):
            q.append(q.popleft())
        else:
            if M == 0:
                break
            q.popleft()
            ans += 1
        
        if M > 0:
            M -= 1
        else:
            M = len(q) - 1
    
    print(ans)
