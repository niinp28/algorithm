# 쇠막대기
# ()(((()())(())()))(())

s = input()
ans = 0
stick = 1
for i in range(1, len(s)):
    if s[i] == '(':
        stick += 1
    else:
        if s[i-1] == '(':
            stick -= 1
            ans += stick
        else:
            ans += 1
            stick -= 1
print(ans)
