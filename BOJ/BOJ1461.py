# 도스관

N, K = map(int, input().split())
book = list(map(int,input().split()))
plus, minus = [], []
for number in book:
    if number > 0:
        plus.append(number)
    else:
        minus.append(number)
plus.sort()
minus.sort(reverse=True)
ans = 0

first = True
while True:
    if plus and minus:
        left, right = minus[-1], plus[-1]
    else:
        if plus:
            left, right = -10001, plus[-1]
        elif minus:
            left, right = minus[-1], 10001
        else:
            break

    if abs(left) < 10001 and abs(right) < 10001:
        status = ''
        if abs(left) < abs(right):
            status = 'right'
            
        else:
            status = 'left'
            
    elif left == -10001:
        status = 'right'
    elif right == 10001:
        status = 'left'

    if status == 'right':
        for _ in range(K):
            if plus:
                plus.pop()
        if first:
            ans += right
            first = False
        else:
            ans += right * 2
    elif status == 'left':
        for _ in range(K):
            if minus:
                minus.pop()
        if first:
            ans += abs(left)
            first = False
        else:
            ans += abs(left) * 2
print(ans)

