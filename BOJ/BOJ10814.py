# 나이순
N = int(input())
answer = []
for i in range(N):
    age, name = input().split()
    answer.append((i, age, name))
answer.sort(key=lambda x: (int(x[1]), x[0]))

for member in answer:
    print(f'{member[1]} {member[2]}')