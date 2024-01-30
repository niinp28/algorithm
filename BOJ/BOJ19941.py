# 햄버거 분배

N, K = map(int, input().split())
current = list(input())
ans = 0

for i in range(len(current)):
    if current[i] == 'P':
        for j in range(max(0, i-K), min(i+K+1, N)):
            if current[j] == 'H':
                current[j] = 'X'
                ans += 1
                break

print(ans)