# 근손실
def dfs(level, total):
    global ans
    if total < 500:
        return
    if level == N:
        ans += 1
        return
    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                result[level] = numbers[i]
                dfs(level+1, total-K+numbers[i])
                check[i] = 0
    

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
result = [0] * len(numbers)
check = [0] * (N+1)
ans = 0
dfs(0, 500)
print(ans)