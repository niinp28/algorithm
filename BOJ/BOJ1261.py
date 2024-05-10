# 알고 스팟
import heapq
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dijkstra(r, c):
    dist = [[float('inf')] * N for _ in range(M)]
    dist[0][0] = 0
    pq = [(0, r, c)]
    while pq:
        cur_d, cur_r, cur_c = heapq.heappop(pq)
        if cur_d > dist[cur_r][cur_c]:
            continue
        
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]
            if (0<=nr<M) and (0<=nc<N):
                distance = cur_d + arr[nr][nc]
                if distance < dist[nr][nc]:
                    dist[nr][nc] = distance
                    heapq.heappush(pq, (distance, nr, nc))
        
    return dist


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

print(dijkstra(0, 0)[M-1][N-1])