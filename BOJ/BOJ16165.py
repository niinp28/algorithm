# 걸그룹 마스터 준석이
N, M = map(int, input().split())
idols = {}
sosok = {}
for _ in range(N):
    group = input()
    n = int(input())
    lst = []
    for _ in range(n):
        mem = input()
        sosok[mem] = group
        lst.append(mem)
    lst.sort()
    idols[group] = lst

for _ in range(M):
    name = input()
    type = int(input())
    if type == 1:
        print(sosok[name])
    else:
        for mem in idols[name]:
            print(mem)