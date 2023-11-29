# 접미사 배열
S = input()
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])
suffix.sort()
for suf in suffix:
    print(suf)