# 비슷한 단어
N = int(input())
target = list(input())
ans = 0

for i in range(N-1):
    comp = target[:]
    word = input()
    cnt = 0
    
    for w in word:
        if w in comp:
            comp.remove(w)
        else:
            cnt += 1
    
    if cnt < 2 and len(comp) < 2:  # 비슷한 단어가 되려면 남은 comp속 요소의 갯수가 1, cnt가 1일때만 성립
        ans += 1

print(ans)
