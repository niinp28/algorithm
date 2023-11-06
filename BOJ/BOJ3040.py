# 백설 공주와 일곱 난쟁이
dwarf = [int(input()) for _ in range(9)]


i = 0
j = len(dwarf)-1
fake = sum(dwarf) - 100
while i < j:
    s = sorted(dwarf)[i] + sorted(dwarf)[j]
    if s < fake:
        i += 1
    elif s > fake:
        j -= 1
    else:
        a, b = sorted(dwarf)[i], sorted(dwarf)[j]
        break
for d in dwarf:
    if d == a or d == b:
        continue
    else:
        print(d)