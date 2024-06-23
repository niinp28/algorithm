# 생태학

d = {}
cnt = 0
while True:
    try:
        species = input().rstrip()
        d[species] = d.get(species, 0) + 1
        cnt += 1

    except EOFError:
        break

for s, c in sorted(d.items()):
    r = (c / cnt) * 100
    print(f'{s} {r:.4f}')