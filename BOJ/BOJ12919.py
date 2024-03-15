# a와 b 2
def recur(word):
    global res
    if len(word) == len(S):
        if word == S:
            res = 1
            return
        return
    if word[-1] == 'A':
        word.pop()
        recur(word)
        word.append('A')
    if word[0] == 'B':
        word.reverse()
        word.pop()
        recur(word)
        word.append('B')
        word.reverse()
    

S = list(input())
T = list(input())
res = 0
recur(T)
print(res)