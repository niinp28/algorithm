# 숫자 만들기
def cal(plus, minus, multi, div, depth, total):
    if depth == len(nums):
        lst.append(total)
        
    if plus:
        cal(plus-1, minus, multi, div, depth+1, total+nums[depth])
    if minus:
        cal(plus, minus-1, multi, div, depth+1, total-nums[depth])
    if multi:
        cal(plus, minus, multi-1, div, depth+1, total*nums[depth])
    if div:
        cal(plus, minus, multi, div-1, depth+1, int(total/nums[depth]))
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ops = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    lst = []
    cal(ops[0], ops[1], ops[2], ops[3], 1, nums[0])
    lst.sort()
    print(f'#{tc} {lst[-1]-lst[0]}')