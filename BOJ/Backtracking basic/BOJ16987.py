# 계란으로 계란치기

def dfs(level, eggs):
    global mx
    # 마지막 계란을 집었을 때
    if level == N:
        cnt = 0
        for i in range(N):
            if eggs[i] <= 0:
                cnt += 1
        if mx < cnt:
            mx = cnt
        return

    # 깨지지 않은 계란을 집었을 때는 계란치기 수행
    if eggs[level] > 0:
        for i in range(N):
            is_all_broken = True
            # 내구도가 0이 아닌 다른  계란일 때
            if eggs[i] > 0 and i != level:
                is_all_broken = False
                eggs[i] -= w[level]
                eggs[level] -= w[i]
                dfs(level+1, eggs)
                eggs[i] += w[level]
                eggs[level] += w[i]
        # 다른 계란들을 다 탐색해봤는데 다 깨져있을 경우
        if is_all_broken:
            dfs(level+1, eggs)

    # 깨진 계란이면 다음 단계로 넘어간다
    else:
        dfs(level+1, eggs)


N = int(input())
s = [0] * N
w = [0] * N
for i in range(N):
    s[i], w[i] = map(int, input().split())
mx = 0

dfs(0, s)
print(mx)