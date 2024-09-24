# 부등호
def dfs(level):
    global cnt, last, first
    if level == N+1:
        cnt += 1
        last = ''.join(map(str, result))
        if cnt == 1:
            first = ''.join(map(str, result))
    
    elif level >= 1:
        for i in range(10):
            if check[i] == 0:
                if setting[level-1] == '<' and result[level-1] < numbers[i]:
                    check[i] = 1
                    result[level] = numbers[i]
                    dfs(level+1)
                    check[i] = 0
                elif setting[level-1] == '>' and result[level-1] > numbers[i]:
                    check[i] = 1
                    result[level] = numbers[i]
                    dfs(level+1)
                    check[i] = 0
                
    else:
        for i in range(10):
            if check[i] == 0:
                check[i] = 1
                result[level] = numbers[i]
                dfs(level+1)
                check[i] = 0
    
  

N = int(input())
setting = list(input().split())
numbers = [i for i in range(10)]
result = [0] * (N+1)
check = [0] * (10)
cnt = 0
last = 0
first = 0
dfs(0)
print(last)
print(first)

