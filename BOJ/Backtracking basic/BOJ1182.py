# 부분수열의 합
def dfs(level, s, r):
    global cnt
    if level == r:
        if sum(rs) == S:
            cnt += 1
    else:
        for i in range(s, len(nums)):
            rs.append(nums[i])
            dfs(level+1, i+1, r)
            rs.pop()
    


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
rs = []
for i in range(N):
    dfs(0, 0, i+1)

print(cnt)