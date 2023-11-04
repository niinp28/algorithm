# 뒤집기
# s의 길이 < 100만
s = input()
chg = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        chg += 1

if chg % 2:
    print(chg//2 + 1)
else:
    print(chg//2)
