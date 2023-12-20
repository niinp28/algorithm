# 센서

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
dist = []
for i in range(len(sensors)-1):
    dist.append(abs(sensors[i]-sensors[i+1]))
dist.sort()

if k >= n:
    print(0)
else:
    for _ in range(k-1):
        dist.pop()
    print(sum(dist))