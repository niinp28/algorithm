
n = int(input())
ans = 0
threes = 0
while n > 0:
    if n % 5 == 0:  # 5의 배수면 몫만큼 더하면 됨
        ans += n//5
        n = 0
    else: # 아니면 3 빼기
        n -= 3
        ans += 1

if n:
    print(-1)
else:
    print(ans)
