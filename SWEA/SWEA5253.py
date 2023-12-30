# 접두어 검색

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())  # 테케 50개 이하, N 3이상, M 3000이하, 스트링 20글자 이하
    a = [input() for _ in range(N)]
    b = [input() for _ in range(M)]
    cnt = 0
    for prefix in b:
        flag = False
        p_len = len(prefix)
        for word in a:
            if word[:p_len] == prefix:
                flag = True
                cnt += 1
                break
    print(f'#{tc} {cnt}')
