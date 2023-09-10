from collections import deque
f, s, g, u, d = map(int, input().split())
# f = 총 층의 갯수
# s = 현재 층
# g = 목적지(goal)
# u, d = up & down

def bfs(s, g, u, d):
    q = deque()
    q.append(s)
    check[s] += 1
    while q:
        a = q.popleft()
        if a == g:

            print(check[a] - 1)
            break

        for i in (a+u, a-d):
            if 1<= i <= f and not check[i]:
                check[i] = check[a] + 1
                q.append(i)

    if not check[g] and s != g:
        print('use the stairs')

check = [0] * (f+1)
bfs(s, g, u, d)
