# A -> B

A, B = map(int, input().split())
cnt = 0
while True:
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else:
            print(-1)
            break
    
    if A == B:
        print(cnt+1)
        break

    if B < A:
        print(-1)
        break
