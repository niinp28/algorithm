# 숫자 카드 2
# 1<=N<=50만, 정수는 +- 1000만
# 1<=M<=50만

N = int(input())
sg_card = list(map(int, input().split()))
M = int(input())
need_check = list(map(int, input().split()))

visited = [0] * 20000001
for card in sg_card:
    visited[card+10000000] += 1

for card in need_check:
    print(visited[card+10000000], end=' ')