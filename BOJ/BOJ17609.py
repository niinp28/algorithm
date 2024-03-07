# 회문

T = int(input())
for _ in range(T):
    word = input()
    s = 0
    e = len(word)-1
    flag = False
    while s < e:
        if word[s] == word[e]:
            s += 1
            e -= 1
        else:
            flag = True
            if s <= e-1:
                tmp = word[:e] + word[e+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            if s+1 <= e:
                tmp = word[:s] + word[s+1:]
                if tmp[:] == tmp[::-1]:
                    print(1)
                    break
            print(2)
            break

    if not flag:
        print(0)

