# 미로 만들기
import heapq
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dijkstra(r, c):
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, r, c)]
    while pq:
        cur_d, cur_r, cur_c = heapq.heappop(pq)
        if cur_d > dist[cur_r][cur_c]:
            continue
        
        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]
            if (0<=nr<N) and (0<=nc<N):
                if arr[nr][nc] == 0:
                    distance = cur_d + 1
                else:
                    distance = cur_d
                if distance < dist[nr][nc]:
                    dist[nr][nc] = distance
                    heapq.heappush(pq, (distance, nr, nc))
        
    return dist


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

print(dijkstra(0, 0)[N-1][N-1])