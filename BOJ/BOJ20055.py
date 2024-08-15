# 컨베이어
from collections import deque
def rotate(L):
    last = L.pop()
    L.appendleft(last)

def move():
    for i in range(N-2, -1, -1):
        if belt[i+1] > 0 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[-1] = 0
    

def add():
    if belt[0] > 0 and robot[0] != 1:
        robot[0] = 1
        belt[0] -= 1
    


N, K = map(int, input().split())
lst = list(map(int, input().split()))
belt = deque(lst)
robot = deque([0] * N)
step = 0

while True:
    step += 1
    # 회전
    rotate(belt)
    rotate(robot)
    robot[-1] = 0

    # 이동
    move()

    # 추가
    add()
    
    # 내구도 계산 및 종료
    if belt.count(0) >= K:
        break
print(step)