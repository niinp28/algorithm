# 문서검색

a = input()
b = input()
i = 0
cnt = 0
while True:
    if len(a[i:i+len(b)]) == len(b):
        if a[i:i+len(b)] == b:
            cnt += 1
            i += len(b)
        else:
            i += 1
    else:
        break
print(cnt)