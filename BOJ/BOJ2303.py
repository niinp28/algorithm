# 숫자 게임

N = int(input())
score = []

for _ in range(N):
    card = list(map(int, input().split()))
    mx = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                tmp = (card[i]+card[j]+card[k]) % 10
                if mx <= tmp:
                    mx = tmp
    score.append(mx)

for i in range(N-1, -1, -1):
    if score[i] == max(score):
        print(i+1)
        break
