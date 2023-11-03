# 회의실 배정

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))

# 첫 번째는 무조건 고름, 정렬해놨기 때문
ans = 1
meeting_end = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= meeting_end:
        ans += 1
        meeting_end = meeting[i][1]
print(ans)