# 톱니바퀴
def process(index, d):
    a, b = arr[index][2], arr[index][6]
    arr[index] = rotation(arr[index], d)
    visited[index] = 1
    if index < 3 and not visited[index+1] and a != arr[index+1][6]:
        process(index+1, -d)

    if index > 0 and not visited[index-1] and b != arr[index-1][2]:
        process(index-1, -d)
    

    
def rotation(gear, d):
    if d == -1:
        return gear[1:] + [gear[0]]
    elif d == 1:
        return [gear[-1]] + gear[:-1]
    


arr = [list(map(int, input())) for _ in range(4)]
n = int(input())
rotate = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for r in rotate:
    idx, direction = r[0]-1, r[1]
    visited = [0] * 4
    process(idx, direction)
    

for i, gear in enumerate(arr):
    if gear[0] == 1:
        ans += 2 ** i

# print(arr)
print(ans)