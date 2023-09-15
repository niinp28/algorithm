n = int(input())
nums = list(map(int, input().split()))
# + - x %
operator = list(map(int, input().split()))

# 메모: 1e9로 설정했더니 틀렸음
# 이유는 답 자체가 +-1e9일 경우 mx 또는 mn 값이 갱신이 안됨!
# 그렇다는 뜻은 정답을 출력할 때 실수형으로 출력되기 때문에 끝에 .0이 붙어서 출력되어 틀림
# 고로 갱신할 mx, mn을 더 큰 숫자로 표기하거나
# 아예 출력할 때 int()로 덮어서 정수형으로 강제로 만들어버리면 된다.
mx = -1e10
mn = 1e10
def calculate(depth, total, plus, minus, multiple, divide):
    global mx, mn
    if depth == n-1:
        mx = max(mx, total)
        mn = min(mn, total)
        return
    
    if plus:
        calculate(depth+1, total + nums[depth+1], plus-1, minus, multiple, divide)
    if minus:
        calculate(depth+1, total - nums[depth+1], plus, minus-1, multiple, divide)
    if multiple:
        calculate(depth+1, total * nums[depth+1], plus, minus, multiple-1, divide)
    if divide:
        calculate(depth+1, int(total / nums[depth+1]), plus, minus, multiple, divide-1)

calculate(0, nums[0], operator[0], operator[1], operator[2], operator[3])
print(mx)
print(mn)