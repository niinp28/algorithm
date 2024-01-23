# 한 줄로 서기

n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
for i in range(n):  # lst에서 키작은 순서대로
    cnt = 0  # cnt 자릿수만큼 띄우고 숫자를 채워 넣기 위한 변수
    for j in range(n):  # ans 배열을 탐색하기 위함
        if cnt == lst[i] and not ans[j]:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans)
