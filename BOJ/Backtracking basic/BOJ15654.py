# N과 M (5)
def dfs(level):
    if level == M:
        print(' '.join(map(str, result)))
    else:
        for i in range(len(numbers)):
            if check[i] == 0:
                check[i] = 1
                result[level] = numbers[i]
                dfs(level+1)
                check[i] = 0
                
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = [0] * M
check = [0] * (len(numbers))
dfs(0)
