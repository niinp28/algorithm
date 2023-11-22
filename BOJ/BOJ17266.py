# 어두운 굴다리
N = int(input()) # 굴다리 길이
M = int(input()) # 가로등 개수
pos = list(map(int, input().split()))

ans = 0 
if M == 1:
    ans = max(pos[0], N-pos[0])
else:
    tmp = 0
    for i in range(M):
        if i == 0:
            tmp = pos[i]
        elif i == M-1:
            tmp = N-pos[i]
        else:
            dis = pos[i]-pos[i-1]
            if dis%2:
                tmp = (dis // 2) + 1
            else:
                tmp = dis // 2
        ans = max(ans, tmp)
print(ans)