# IOIOI

N = int(input())
M = int(input())
S = input()
check = ''
cnt = 0

for idx in range(2*N+1):
    if idx % 2:
        check += 'O'
    else:
        check += 'I'

for i in range(M):
    if S[i:i+2*N+1] == check:
        cnt += 1
print(cnt)