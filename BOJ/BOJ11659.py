# 구간 합 구하기 4
N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + num_lst[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])

