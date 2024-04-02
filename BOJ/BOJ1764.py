# 듣보잡

n, m = map(int, input().split())
graph = {}
ans = []
for _ in range(n):
    person = input()
    graph[person] = graph.get(person, 0) + 1
for _ in range(m):
    person = input()
    graph[person] = graph.get(person, 0) + 1
for name, n in graph.items():
    if n == 2:
        ans.append(name)

ans.sort()
print(len(ans))
for a in ans:
    print(a)