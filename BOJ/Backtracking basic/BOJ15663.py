# N과 M (9)
def dfs(level):
    if level == M:
        answers.append(result[:])
    else:
        for i in range(len(numbers)):
            if not check[i]:
                check[i] = 1
                result[level] = numbers[i]
                dfs(level+1)
                check[i] = 0
    

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = [0] * M
check = [0] * len(numbers)
answers = []
dfs(0)
answers.sort()
for i in range(len(answers)):
    if i == 0:
        print(' '.join(map(str, answers[i])))
    else:
        if answers[i] != answers[i-1]:
            print(' '.join(map(str, answers[i])))