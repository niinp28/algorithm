# 나무 자르기

n, m = map(int, input().split())
namu = list(map(int, input().split()))
s = 1
e = max(namu)
ans = 0
'''
while s <= e:
    mid = (s+e) // 2
    # print(s, e, mid)
    tmp = 0
    for tree in namu:
        if tree > mid:
            tmp += (tree - mid)
    # print(tmp)
    if tmp == m:
        if ans < mid:
            ans = mid
            break
    elif tmp > m:
        s = mid+1
        if ans < mid:
            ans = mid
    else:
        e = mid
    # print(ans)    
print(ans)

'''
while s <= e:
    mid = (s+e)//2
    tmp = 0
    for tree in namu:
        if tree >= mid:
            tmp += tree - mid
    
    if tmp >= m:
        s = mid + 1
    else:
        e = mid -1
print(end)
