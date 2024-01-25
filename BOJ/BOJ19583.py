
s, e, q = input().split()
cnt = 0
present = set()
while True:
    try:
        time, name = input().split()
        if int(time[:2] + time[3:]) <= int(s[:2] + s[3:]):
            present.add(name)
        elif int(e[:2]+e[3:]) <= int(time[:2] + time[3:]) <= int(q[:2]+q[3:]) and name in present:
            present.remove(name)
            cnt += 1
    except:
        break

print(cnt)

'''
22:00 23:00 23:30
21:30 malkoring
21:33 tolelom
21:34 minjae705
21:35 hhan14
21:36 dicohy27
21:40 906bc
23:00 906bc
23:01 tolelom
23:10 minjae705
23:11 hhan14
23:20 dicohy27
'''