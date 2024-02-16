# 올림픽

N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))

graph = {}
info = nations[0][1:]
cnt = 1
increase = 0
for nation in nations:
    nation_id = nation[0]
    tmp = nation[1:]
    if info == tmp:
        graph[nation_id] = cnt
        increase += 1
    else:
        cnt += increase
        graph[nation_id] = cnt
        info = tmp
        increase = 0

print(graph[K])