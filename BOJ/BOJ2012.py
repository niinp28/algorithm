# 등수 매기기

N = int(input())

lst = [int(input()) for _ in range(N)]
expected = [i for i in range(1, N+1)]
lst.sort()

ans = 0
for i in range(len(lst)):
    ans += abs(expected[i]-lst[i])
print(ans)