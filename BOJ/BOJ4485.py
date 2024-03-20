
# 젤다
'''
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, v):
    global mn
    if v > mn:
        return
    
    if r == N-1 and c == N-1:
        if mn > v:
            mn = v
            return
        
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0<=nr<N) and (0<=nc<N) and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, v+arr[nr][nc])
            visited[nr][nc] = 0
    
t = 1
while 1:
    N = int(input())
    if N:
        arr = [list(map(int, input().split())) for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        mn = 1e9
        visited[0][0] = 1
        dfs(0, 0, arr[0][0])
        print(f'Problem {t}: {mn}')
        t += 1
    else:
        break
'''
'''
위 알고리즘 틀림! -> 시간초과
'''

import heapq
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dij():
    global mn
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = arr[0][0]
    pq = [(arr[0][0], 0, 0)]  # 우선순위 큐(Priority Queue), (비용, 행, 열)로 표기
    while pq:
        cost, r, c = heapq.heappop(pq)

        # distance[r][c]: 해당 정점까지 최단 거리, cost: 현재 루트의 거리
        # 최단 거리보다 현재 루트가 비효율적이면 건너뛴다.
        if distance[r][c] < cost:  
            continue

        if r == N-1 and c == N-1:
            mn = cost
            return

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                new_cost = cost + arr[nr][nc]
                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))




t = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = float('inf')
    dij()
    print(f'Problem {t}: {mn}')
    t += 1