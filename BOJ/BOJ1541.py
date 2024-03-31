# 잃어버린 괄호

lst = input().split('-')
calculated = []

for el in lst:
    total = 0
    tmp = map(int, el.split('+'))
    for number in tmp:
        total += number
    calculated.append(total)

print(calculated[0] - sum(calculated[1:]))