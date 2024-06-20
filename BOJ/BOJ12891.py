# DNA 

S, P = map(int, input().split())
string = input()
a, c, g, t = map(int, input().split())
ans = 0

tmp = [0, 0, 0, 0]
substr = string[:P]
for al in substr:
    if al == 'A':
        tmp[0] += 1
    elif al == 'C':
        tmp[1] += 1
    elif al == 'G':
        tmp[2] += 1
    elif al == 'T':
        tmp[3] += 1
if a <= tmp[0] and c <= tmp[1] and g <= tmp[2] and t <= tmp[3]:
    ans += 1

for i in range(P, S):
    if string[i] == 'A':
        tmp[0] += 1
    elif string[i] == 'C':
        tmp[1] += 1
    elif string[i] == 'G':
        tmp[2] += 1
    elif string[i] == 'T':
        tmp[3] += 1

    if string[i-P] == 'A':
        tmp[0] -= 1
    elif string[i-P] == 'C':
        tmp[1] -= 1
    elif string[i-P] == 'G':
        tmp[2] -= 1
    elif string[i-P] == 'T':
        tmp[3] -= 1
    
    if a <= tmp[0] and c <= tmp[1] and g <= tmp[2] and t <= tmp[3]:
        ans += 1
print(ans)