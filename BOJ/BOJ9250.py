from collections import deque

def bfs():
    q = deque()
    q.append(home)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 목적지까지 도착할 수 있는 경우
        if abs(x - destination[0]) + abs(y - destination[1]) <= 1000:
            print('happy')
            return
        # 편의점을 들러야 하는 경우
        for i in range(n):
            if not visited[i]:
                nx = store[i][0]
                ny = store[i][1]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1
    print('sad')
    return

tc = int(input())
for _ in range(tc):
    n = int(input()) # 편의점 갯수
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    destination = list(map(int, input().split()))
    visited = [0 for _ in range(n+2)]
    bfs()
    