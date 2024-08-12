# 숫자고르기
def dfs(now, initial):
    visited[now] = 1
    nxt = nums[now]
    if not visited[nxt]:
        dfs(nxt, initial)
    elif visited[nxt] and nxt == initial:
        ans.append(nxt)
    


N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
ans = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    dfs(i, i)
print(len(ans))
for i in ans:
    print(i)