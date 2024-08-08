# 미친 아두이노
from pprint import pprint
dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
def move(r, c, direction):
    global jr, jc, arduinos
    nr = r + dr[int(direction)-1]
    nc = c + dc[int(direction)-1]
    board[r][c] = '.'
    if board[nr][nc] == '.':
        board[nr][nc] = 'I'
        jr, jc = nr, nc
    else:
        return False
    new_ard = set()
    
    for ard in arduinos:
        ar, ac = ard[0], ard[1]
        if ar == jr:
            nar = ar
            if ac > jc:
                nac = ac - 1
            else:
                nac = ac + 1
                
        elif ac == jc:
            nac = ac
            if ar > jr:
                nar = ar - 1
            else:
                nar = ar + 1
        else:
            if ar > jr and ac > jc:  
                nar = ar - 1
                nac = ac - 1
            elif ar > jr and ac < jc:
                nar = ar - 1
                nac = ac + 1
            elif ar < jr and ac < jc:
                nar = ar + 1
                nac = ac + 1
            else:
                nar = ar + 1
                nac = ac - 1
        board[ar][ac] = '.'
        bomb[ar][ac] -= 1
        bomb[nar][nac] += 1
        new_ard.add((nar, nac))
    
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 1:
                board[i][j] = 'R'
            elif bomb[i][j] > 1:
                bomb[i][j] = 0
                new_ard.remove((i, j))
                
    
    arduinos = new_ard
    pprint(board)
    print()
    return True
    



R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
bomb = [[0] * C for _ in range(R)]
command = input()
turn = 0
arduinos = []
jr, jc = 0, 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'I':
            jr, jc = i, j
            bomb[jr][jc] = 1
        elif board[i][j] == 'R':
            arduinos.append((i, j))
            bomb[i][j] = 1

for i in range(len(command)):
    ans = move(jr, jc, command[i])
    if not ans:
        print(f'kraj {i+1}')
        break
else:
    for row in board:
        print(''.join(row))