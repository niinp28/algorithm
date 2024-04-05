def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

def dfs(index, prev):
    global ans
    if index >= N:
        ans = max(ans, prev)
        return
    
    if index + 3 < N:  # 괄호로 묶을 수 있는 경우
        dfs(index+4, cal(prev, cal(susik[index+1],susik[index+3],susik[index+2]), susik[index]))
    
    dfs(index+2, cal(prev, susik[index+1], susik[index]))  # 그냥 계산



N = int(input())
susik = list(map(lambda x: int(x) if x.isdigit() else x, input()))
ans = -1e9

if N == 1:
    ans = susik[0]
else:
    dfs(1, susik[0])

print(ans)