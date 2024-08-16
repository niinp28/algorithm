# 스카이라인 쉬운거

n = int(input())
skyline = [tuple(map(int,input().split())) for _ in range(n)]
stack = []
height = 0
ans = 0
for x, building in skyline:
    if x == 1:
        if building:
            stack.append(building)
            height = building
    else:
        if building == 0:
            height = building
            while stack:
                stack.pop()
                ans += 1
            
        if building > height:
            stack.append(building)
            height = building
        elif building < height:
            height = building
            while stack:
                el = stack.pop()
                ans += 1
                if el <= height:
                    stack.append(el)
                    ans -= 1
                    break
            if not stack:
                stack.append(building)
            else:
                if building > stack[-1]:
                    stack.append(building)
    
print(ans + len(stack))
'''
10
1 1
2 2
5 0
6 3
8 1
11 0
15 2
17 3
20 2
22 1
'''