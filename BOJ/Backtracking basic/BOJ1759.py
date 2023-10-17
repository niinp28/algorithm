#암호 만들기
def dfs(level, start):
    v_cnt = 0
    c_cnt = 0
    if level == L:
        for el in rs:
            if el in vowel:
                v_cnt += 1
            elif el in cons:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(rs))
        v_cnt, c_cnt = 0, 0
    else:
        for i in range(start, len(alphabet)):
            rs[level] = alphabet[i]
            dfs(level+1, i+1)
    


L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
vowel = []
cons = []
for a in alphabet:
    if a in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(a)
    else:
        cons.append(a)
rs = [0] * L
dfs(0, 0)
