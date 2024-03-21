# 1로 만들기

N = int(input())
dp = [0] * 1000001

for i in range(2, N+1):

    dp[i] = dp[i-1] + 1

    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])

ans = [N]
present = N
tmp = dp[N]-1

for i in range(N, 0, -1):
    if dp[i] == tmp and (i+1 == present or i*2 == present or i*3 == present):
        present = i
        ans.append(i)
        tmp -= 1
print(*ans)