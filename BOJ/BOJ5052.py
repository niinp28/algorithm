# 전화번호 목록

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input() for _ in range(n)]
    numbers.sort()
    validity = 1
    for i in range(n-1):
        length = len(numbers[i])
        if numbers[i] == numbers[i+1][:length]:
            validity = 0
            break
    if validity:
        print('YES')
    else:
        print('NO')