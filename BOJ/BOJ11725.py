# 트리의 부모 찾기
N = int(input())
graph = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]

visited = [0] * (N+1)
tree = {}
stack = [1]
while stack:
    a = stack.pop()
    visited[a] = 1
    for num in graph[a]:
        if not visited[num]:
            stack.append(num)
            tree[num] = a
for i in range(2, N+1):
    print(tree[i])
