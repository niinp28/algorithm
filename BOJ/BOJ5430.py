from collections import deque
T = int(input())
for _ in range(T):
    f = input()
    n = int(input())
    lst = deque((input().rstrip(']').lstrip('[').split(',')))
    isError = False
    rev = 0
    if n:
        lst = deque((map(int, lst)))
    else:
        lst = deque()
    for c in f:
        if c == 'R':  # 뒤집기
            rev += 1
        else:
            if lst:
                if rev % 2:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                isError = True
                break
    if isError:
        print('error')
    else:
        if rev % 2:
            lst.reverse()
            print('[' +','.join(map(str, lst)) + ']')
        else:
            print('[' +','.join(map(str, lst)) + ']')