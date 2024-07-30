# Olympiad pizza

n = int(input())
feed = list(map(int, input().split()))
t = 0
ans = [0] * n
while max(feed):
    for i in range(len(feed)):
        if feed[i] == 0:
            continue
        else:
            feed[i] -= 1
            t += 1
            if not feed[i]:
                ans[i] = t
print(' '.join(map(str, ans)))
