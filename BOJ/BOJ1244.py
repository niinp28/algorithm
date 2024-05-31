# 스위치 켜고 끄기
def male(k):
    for i in range(1, len(switches)):
        if i % k == 0:
            change(i)

def female(k):
    change(k)
    i = 1
    while True:
        if (1 <= k+i <len(switches)) and (1 <= k-i < len(switches)) and switches[k+i] == switches[k-i]:
            change(k+i)
            change(k-i)
            i += 1
        else:
            break

def change(k):
    if switches[k] == 0:
        switches[k] = 1
    elif switches[k] == 1:
        switches[k] = 0
n = int(input())
switches = [0] + list(map(int, input().split()))
m = int(input())
command = [tuple(map(int, input().split())) for _ in range(m)]

for gender, number in command:
    if gender == 1:
        male(number)
    else:
        female(number)

for i in range(1, n+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()