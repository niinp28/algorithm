# 시그널
from pprint import pprint
N = int(input())
line = N // 5
signal = input()
arr = []
numbers = [
    ['#####', '#...#', '#####'], # 0
    ['#####'],                   # 1
    ['#.###', '#.#.#', '###.#'], # 2
    ['#.#.#', '#.#.#', '#####'], # 3
    ['###..', '..#..', '#####'], # 4
    ['###.#', '#.#.#', '#.###'], # 5
    ['#####', '#.#.#', '#.###'], # 6
    ['#....', '#....', '#####'], # 7
    ['#####', '#.#.#', '#####'], # 8
    ['###.#', '#.#.#', '#####'], # 9
]
for i in range(5):
    arr.append(signal[line*i:line*i+line])

arr = list(map(list, zip(*arr)))
ans = ''
tmp = []
arr.append(['.....'])
for row in arr:
    letter = ''.join(row)
    if letter != '.....':
        tmp.append(letter)
    else:
        if tmp:
            for i in range(10):
                if tmp == numbers[i]:
                    ans += str(i)
                    tmp = []
print(ans)