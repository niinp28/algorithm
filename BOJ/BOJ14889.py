# 스타트와 링크: 백트래킹
import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
res = sys.maxsize

def dfs(depth, index):
    global res
    if depth == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        res = min(res, abs(start-link))
        return
    for i in range(index, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

dfs(0, 0)
print(res)