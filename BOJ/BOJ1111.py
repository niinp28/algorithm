# IQ TEST

N = int(input())
lst = list(map(int, input().split()))

if N == 1:
    print('B')
elif N == 2:
    if lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')
else:
    if lst[0] - lst[1] == 0:
        a = 0
    else:
        a = (lst[1]-lst[2]) // (lst[0]-lst[1])
    b = lst[1] - lst[0] * a

    for i in range(N-1):
        nxt = lst[i] * a + b
        if lst[i+1] != nxt:
            print('B')
            exit()
    print(lst[-1]*a+b)