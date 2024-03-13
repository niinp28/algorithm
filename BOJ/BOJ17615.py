# 볼 모으기

n = int(input())
m = list(input())
ans = []
b = 0
r = 0
cnt = 0

# 빨간공 보내기(우)
for i in range(n):
    if m[i] == 'R':
        r += 1
    
    if m[i] == 'B' and r:
        cnt += r
        r = 0
ans.append(cnt)

# 파란공 보내기(우)
cnt = 0
for i in range(n):
    if m[i] == 'B':
        b += 1
    
    if m[i] == 'R' and b:
        cnt += b
        b = 0
ans.append(cnt)

r = 0
b = 0
cnt = 0

m.reverse() # 좌측으로 보내기 => 뒤집어서 순회
for i in range(n):
    if m[i] == 'R':
        r += 1
    
    if m[i] == 'B' and r:
        cnt += r
        r = 0
ans.append(cnt)
cnt = 0
for i in range(n):
    if m[i] == 'B':
        b += 1
    
    if m[i] == 'R' and b:
        cnt += b
        b = 0
ans.append(cnt)
print(min(ans))