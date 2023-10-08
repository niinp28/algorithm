# 요리사
from itertools import combinations as com

def synergy(arr, case):
    score = 0
    for ing1, ing2 in com(case, 2):
        score += arr[ing1][ing2] + arr[ing2][ing1]
    return score

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 50000
    # 조합으로 팀 나누기
    for c in com(range(N), N//2):
        other = list(set(range(N)) - set(c))
        syn1 = synergy(arr, c)
        syn2 = synergy(arr, other)
        res = abs(syn1 - syn2)
        if mn >= res:
            mn = res
    
    print(f'#{tc} {mn}')