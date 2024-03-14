# 회전 초밥

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
mx = 0

for i in range(N):
    if i+k > N:
        tmp = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
    else:
        tmp = len(set(sushi[i:i+k] + [c]))
    
    if mx < tmp:
        mx = tmp
print(mx)