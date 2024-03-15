# a와 b 2
def recur(word):
    global flag
    if len(word) == len(T):
        if word == T:
            flag = True
            return
    else:
        word1 = word + 'A'
        recur(word1)
        word2 = word + 'B'
        word3 = word2[::-1]
        recur(word3)
    

S = input()
T = input()
flag = False
recur(S)

if flag:
    print(1)
else:
    print(0)