# 회사에 있는 사람

n = int(input())
worker = {}
names = set()
for _ in range(n):
    name, status = input().split()
    worker[name] = status
    names.add(name)

nameslst = list(names)
nameslst.sort(reverse=True)

for nm in nameslst:
    if worker[nm] == 'leave':
        continue
    else:
        print(nm)