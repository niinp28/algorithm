# 경사로
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = list(map(list, zip(*arr)))
ans = 0

for road in (arr+arr2):
    visited = [0] * n
    flag = True
    for i in range(n-1):
        if abs(road[i]-road[i+1]) > 1:
            break

        if road[i] < road[i+1]:
            for j in range(i, i-m, -1):
                # 경사로 놔야하는데 경계선보다 길이가 길 경우
                # 경사로 길이 범위 내에서 높이가 달라지는 경우
                # 이미 놓은 경사로 구간인 경우
                # 할 필요 없음!!
                if j < 0 or road[j] != road[i] or visited[j] == 1:
                    flag = False
                    break
                visited[j] = 1

        elif road[i] > road[i+1]:
            for j in range(i+1, i+1+m):
                if j >= n or road[j] != road[i+1] or visited[j] == 1:
                    flag = False
                    break
                visited[j] = 1
        if not flag:
            break
    else:
        ans += 1

print(ans)