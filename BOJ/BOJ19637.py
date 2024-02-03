# if문좀 대신써줘
import sys

N, M = map(int, input().split())  # 10의 5승 이하

score = []
for i in range(N):
    s, n = input().split()
    n = int(n)
    score.append([s, n])
score.sort(key=lambda x: x[1])  # 오름차순

check = [int(input()) for _ in range(M)]
for char in check:
    start = 0
    end = N-1
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if char <= int(score[mid][1]):
            res = mid
            end = mid -1
        else:
            start = mid + 1
    print(score[start][0])

    
    