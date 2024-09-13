from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


N, M, P = map(int, input().split())
available = [0] + list(map(int, input().split()))
arr = [list(input()) for _ in range(N)]
res = [0] * (P+1)

castle = [deque() for _ in range(P+1)]
for i in range(N):
    for j in range(M):
        if arr[i][j].isdigit():
            castle[int(arr[i][j])].append((i, j))
            res[int(arr[i][j])] += 1

while True:
    is_moved = True
    for player in range(1, P+1):
        if not castle[player]:
            continue

        q = castle[player]
        for _ in range(available[player]):
            if not q:
                break
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if (0<=nr<N) and (0<=nc<M) and arr[nr][nc] == '.':
                        arr[nr][nc] = str(player)
                        q.append((nr, nc))
                        res[player] += 1
                        is_moved = False
    if is_moved:
        break
print(*res[1:])




