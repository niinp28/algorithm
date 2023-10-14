# N과 M (6)
def dfs(level, start):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(start, len(numbers)):
            result[level] = numbers[i]
            dfs(level+1, i+1)
    

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = [0] * M
dfs(0, 0)