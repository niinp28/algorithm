# N과 M (10)
def dfs(level, start):
    if level == M:
        answers.append(result[:])
    else:
        for i in range(start, len(numbers)):
            result[level] = numbers[i]
            dfs(level+1, i+1)
    

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = [0] * M
answers = []
dfs(0, 0)
answers.sort()
for i in range(len(answers)):
    if i == 0:
        print(' '.join(map(str, answers[i])))
    else:
        if answers[i] != answers[i-1]:
            print(' '.join(map(str, answers[i])))