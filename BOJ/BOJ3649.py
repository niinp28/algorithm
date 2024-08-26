# 로봇 프로젝트
while True:
    try:
        x = int(input())
        width = x * (10 ** 7)
        n = int(input())
        screw = [int(input()) for _ in range(n)]
        screw.sort()
        ans = []

        s = 0
        e = len(screw)-1
        while s < e:
            total = screw[s] + screw[e]
            if total == width:
                ans.append((s, e))
                break
            elif total < width:
                s += 1
            elif total > width:
                e -= 1
        if ans:
            print(f'yes {screw[ans[-1][0]]} {screw[ans[-1][1]]}')
        else:
            print('danger')
    except:
        break
