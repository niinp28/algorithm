# 텀 프로젝트
import sys
sys.setrecursionlimit(100000)

def dfs(start):
    global rs
    visited[start] = 1
    team.append(start)
    nxt = lst[start]
    if visited[nxt]:
        if nxt in team:
            rs += len(team[team.index(nxt):])
            return
    else:
        dfs(nxt)
    

T = int(input())
for _ in range(T):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    rs = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(n-rs)