# if문좀 대신써줘

N, M = map(int, input().split())  # 10의 5승 이하

score = []
for i in range(N):
    s, n = input().split()
    n = int(n)
    if len(score) == 0 or n > score[-1][1]:  # 없으면 넣기, 있으면 기준 점수가 기존에 있던 것 보다 클 때 넣기
        score.append([s, n])
score.sort(key=lambda x: int(x[1])) #오름차순

check = [int(input()) for _ in range(M)]
for char in check:
    start = 0
    end = N
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if char <= int(score[mid][1]):
            res = mid
            end = mid -1
        else:
            start = mid + 1
    print(score[res][0])

    
    