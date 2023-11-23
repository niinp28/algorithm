# 그룹 단어 체커

N = int(input())
words = [input() for _ in range(N)]
cnt = 0
for word in words:
    alpha = []
    isGroup = True
    for i in range(len(word)):
        if not i:
            alpha.append(word[i])
        else:
            if word[i] == word[i-1]:
                continue
            else:
                if word[i] in alpha:
                    isGroup = False
                    break
                else:
                    alpha.append(word[i])
    if isGroup:
        cnt += 1
    
print(cnt)

                