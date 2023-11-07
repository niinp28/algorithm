from collections import deque
T = int(input())
for tc in range(T):
    N = int(input())
    tong = list(map(int, input().split()))
    tong.sort()
    q = deque()
    q.append(tong[-1])
    for i in range(len(tong)-2, -1, -1):
        if i % 2:
            q.append(tong[i])
        else:
            q.appendleft(tong[i])
    tmp = 0
    for i in range(len(q)):
        if i == len(q)-1:
            if tmp < abs(q[i] - q[0]):
                tmp = abs(q[i] - q[0])
        else:
            if tmp < abs(q[i] - q[i+1]):
                tmp = abs(q[i] - q[i+1])
    print(tmp)