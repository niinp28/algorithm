# N과 M (11)
def dfs(level):
    if level == M:
        answers.append(result[:])
    else:
        for i in range(len(numbers)):
            result[level] = numbers[i]
            dfs(level+1)
    

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = [0] * M
answers = []
dfs(0)
answers.sort()
for i in range(len(answers)):
    if i == 0:
        print(' '.join(map(str, answers[i])))
    else:
        if answers[i] != answers[i-1]:
            print(' '.join(map(str, answers[i])))