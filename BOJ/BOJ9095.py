# 1,2,3 더하기
T = int(input())
for tc in range(T):
    n = int(input())
    dp = [0] * 11
    for i in range(len(dp)):
        if i == 0:
            continue
        elif i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
            
        
