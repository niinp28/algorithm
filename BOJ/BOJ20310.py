# 타노스

s = list(input())
zero = s.count('0')
one = s.count('1')

cnt = 0
for i in s:
    if cnt == one // 2:
        break
    if i == '1':
        s.remove(i)
        cnt += 1

cnt = 0
s = s[::-1]
for i in s:
    if cnt == zero // 2:
        break
    if i == '0':
        s.remove(i)
        cnt += 1

s = s[::-1]
print(''.join(s))