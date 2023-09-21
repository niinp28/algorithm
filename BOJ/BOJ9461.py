# 파도반 수열
T = int(input())
lst = [1, 1, 1]
for n in range(97):
    a = lst[n] + lst[n+1]
    lst.append(a)
for _ in range(T):
    print(lst[int(input())-1])
