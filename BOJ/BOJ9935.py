# 문자열 폭발

st = input()
bomb = input()

while bomb in st:
    st = st.replace(bomb, '')

if st:
    print(st)
else:
    print('FRULA')