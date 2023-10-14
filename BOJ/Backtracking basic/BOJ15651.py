# N과 M (3)
# 중복순열
def dfs(level):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(len(numbers)):
            result[level] = numbers[i]
            dfs(level+1)
    

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = [0] * M
dfs(0)
