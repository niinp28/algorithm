# 트럭

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

q = [0] * w
t = 0

while q:
    t += 1
    q.pop(0)
    if trucks:
        if sum(q) + trucks[0] <= L:
            q.append(trucks.pop(0))
        else:
            q.append(0)
print(t)