lst = [int(input()) for _ in range(3)]

if sum(lst) == 180:
    if len(set(lst)) == 1:
        print('Equilateral')
    elif len(set(lst)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')