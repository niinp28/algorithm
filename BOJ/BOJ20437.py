# 문자열 게임2

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    graph = {}
    cur = 0
    # 알파벳 갯수 저장
    for i in range(len(W)):
        graph[W[i]] = graph.get(W[i], 0) + 1
    
    check_graph = {}
    check = False
    mn = len(W)
    mx = -1

    for i in range(len(W)):
        if graph[W[i]] < K:
            continue
        
        else:
            check = True  # 정답이 있는 테케임
            check_graph[W[i]] = check_graph.get(W[i], []) + [i]  #인덱스 저장
    
    for k, v_lst in check_graph.items():
        for i in range(len(v_lst)-K+1):
            mx = max(mx, v_lst[i+K-1]-v_lst[i]+1)
            mn = min(mn, v_lst[i+K-1]-v_lst[i]+1)
    if check:
        print(mn, mx)
    else:
        print(-1)