# 돌 게임 3
n = int(input())

if n == 1:
    print('SK')
elif n == 2:
    print('CY')
elif n == 3:
    print('SK')
elif n == 4:
    print('SK')
else:
    dp = [-1] * (n+1)  #dp[n]은 n개의 돌이 남은 시점을 이야기함
    dp[1] = 'SK'    # 1개의 돌이 남았으므로 상근 승
    dp[2] = 'CY'    
    dp[3] = 'SK'    
    dp[4] = 'SK'  

    for i in range(5, n+1):
        # 돌이 1개 혹은 3개, 4개 남은 상황일 때
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
    print(dp[n])