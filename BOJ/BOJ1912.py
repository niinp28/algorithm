# 연속합
n = int(input())
lst = list(map(int, input().split()))

cur = mx = lst[0]
for num in lst[1:]:
    cur = max(num, cur+num)
    mx = max(mx, cur)
    
print(mx)