# IOIOI

N = int(input())
M = int(input())
S = input()
check = ''
cnt = 0  #OI 갯수
index = 0
ans = 0

while index < M-1:
    if S[index: index+3] == 'IOI':
        cnt += 1
        index += 2
        if cnt == N:  # P1 = 'IOI', P2 = 'IOIOI'이므로 N은 OI의 갯수이다
            ans += 1
            cnt -= 1
    else:
        index += 1
        cnt = 0
print(ans)