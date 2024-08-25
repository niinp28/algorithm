# 문자열 복사

S = input()
P = input()
ans = 0
s = 0
e = 1

while len(P) > 0:
    while P[s:e] in S:
        e += 1
        if e > len(P):
            break
    ans += 1
    P = P[e-1:]
    s = 0
    e = 1
print(ans)
