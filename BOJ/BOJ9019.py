# DSLR
from collections import deque
def D(num):
    return (num * 2) % 10000
    
def S(num):
    return (num-1) % 10000

def L(num):
    return num // 1000 + (num % 1000) * 10

def R(num):
    return num // 10 + (num % 10) * 1000

def bfs(n):
    q = deque()
    q.append([n, ''])
    visited[n] = 1
    while q:
        number, command = q.popleft()
        if number == goal:
            print(command)
            break

        d = D(number)
        s = S(number)
        l = L(number)
        r = R(number)
        if not visited[d]:
            visited[d] = 1
            q.append([d, command + 'D'])
        if not visited[s]:
            visited[s] = 1
            q.append([s, command + 'S'])
        if not visited[l]:
            visited[l] = 1
            q.append([l, command + 'L'])
        if not visited[r]:
            visited[r] = 1
            q.append([r, command + 'R'])

    

T = int(input())
for _ in range(T):
    start, goal = map(int, input().split())
    visited = [0 for _ in range(10001)]
    bfs(start)