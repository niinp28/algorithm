# 로프
n = int(input())
k = [int(input()) for _ in range(n)]
k.sort()

ans = []
for num in k:
    ans.append(num*n)
    n -= 1
print(max(ans))