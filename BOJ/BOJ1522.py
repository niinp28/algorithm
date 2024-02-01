# 문자열 교환
string = input()
total_a = string.count('a')

mx = 0
cur = 0

# 초기 윈도우
for i in range(len(string)):
    if i < total_a:
        if string[i] == 'a':
            cur += 1
    else:
        break

mx = cur

# 슬라이딩 윈도우 이동
for i in range(len(string)):
    if string[i] == 'a':
        cur -= 1
    if string[(i + total_a) % len(string)] == 'a':
        cur += 1
    
    mx = max(mx, cur)

print(total_a - mx)