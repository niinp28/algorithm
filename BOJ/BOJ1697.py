from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        # 도착
        if x == K:
            print(check[K])
            break
        # 탐색
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and check[i] == 0:
                check[i] = check[x] + 1
                q.append(i)
    

N, K = map(int, input().split())
cnt = 0
check = [0] * (100001)
bfs()