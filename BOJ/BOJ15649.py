# N 과 M
def dfs(level):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                result[level] = numbers[i]
                dfs(level+1)
                check[i] = 0
    

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = [0] * M
check = [0] * (N+1)
dfs(0)