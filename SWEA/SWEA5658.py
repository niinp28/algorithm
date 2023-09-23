# 모의 SW 역량테스트: 보물상자 비밀번호
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    group = N // 4
    s = input()
    lst = []
    new_lst = []
    for _ in range(group):
        for i in range(4):
            lst.append(s[i*group: (i+1)*group])
        s = s[-1] + s[:-1]
    for number in list(set(lst)):
        new_lst.append(int(number, 16))
    print(f'#{tc} {sorted(new_lst)[-K]}')
