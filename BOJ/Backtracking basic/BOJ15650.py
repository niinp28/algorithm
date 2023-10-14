# N과 M (2)
# 조합
def dfs(level, start):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(start, len(numbers)):
            result[level] = numbers[i]
            dfs(level+1, i+1)
    

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = [0] * M
dfs(0, 0)
