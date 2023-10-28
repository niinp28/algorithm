# 상어 초등학교
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bachi(student, v):
    st_num = student[0]
    st_like = student[1:]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                like = 0
                empty = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in st_like:
                            like += 1
                        if arr[nr][nc] == 0:
                            empty += 1
                v.append((like, empty, r, c))
    v.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    arr[v[0][2]][v[0][3]] = st_num
    return


N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
arr = [[0]*N for _ in range(N)]
s = sorted(students, key=lambda x: x[0])

for student in students:
    bachi(student, [])
ans = 0
for i in range(N):
    for j in range(N):
        n = 0
        for d in range(4):
            ni = i + dr[d]
            nj = j + dc[d]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in s[arr[i][j]-1][1:]:
                    n += 1
        if n == 1:
            ans += 1
        elif n == 2:
            ans += 10
        elif n == 3:
            ans += 100
        elif n == 4:
            ans += 1000

print(ans)