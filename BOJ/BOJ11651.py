# 좌표 정렬하기 2
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))
for c in lst:
    print(' '.join(map(str, c)))