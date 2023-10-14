# N-queen
def is_possible(level):
    for i in range(level):
        if row[level] == row[i] or abs(row[level] - row[i]) == abs(level - i):
            return False
    return True

def dfs(level):
    global cnt
    if level == N:
        cnt += 1
        return
    else:
        for i in range(N):
            row[level] = i
            if is_possible(level) == True:
                dfs(level+1)
        
    


N = int(input())
row = [0] * N
cnt = 0
dfs(0)
print(cnt)