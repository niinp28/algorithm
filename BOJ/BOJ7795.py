# 먹을 것인가 먹힐 것인가
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    group_A = list(map(int, input().split()))
    group_B = list(map(int, input().split()))
    group_A.sort(reverse=True)
    group_B.sort(reverse=True)
    p = 0
    ans = 0
    # print(group_A, group_B)
    for i in range(len(group_A)):

        while True:
            if p == len(group_B):
                break

            if group_A[i] > group_B[p]:
                ans += len(group_B[p:])
                break
            else:
                p += 1

    print(ans)