# 결혼식

n = int(input())  # 2<=n<=500
m = int(input())  # 1<=m<=10000
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]


invited = set()
if graph.get(1) == None:
    print(0)
else:
    for friend in graph[1]:
        invited.add(friend)
        for ff in graph[friend]:
            invited.add(ff)
    print(len(invited)-1)
