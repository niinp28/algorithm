# # 미친 아두이노
# dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
# dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
# def move(r, c, direction):
#     global jr, jc, arduinos
#     nr = r + dr[int(direction)-1]
#     nc = c + dc[int(direction)-1]
#     board[r][c] = '.'
#     if board[nr][nc] == '.':
#         board[nr][nc] = 'I'
#         jr, jc = nr, nc
#     else:
#         return False
#     new_ard = set()
    
#     for ard in arduinos:
#         ar, ac = ard[0], ard[1]
#         if ar == jr:
#             nar = ar
#             if ac > jc:
#                 nac = ac - 1
#             else:
#                 nac = ac + 1
                
#         elif ac == jc:
#             nac = ac
#             if ar > jr:
#                 nar = ar - 1
#             else:
#                 nar = ar + 1
#         else:
#             if ar > jr and ac > jc:  
#                 nar = ar - 1
#                 nac = ac - 1
#             elif ar > jr and ac < jc:
#                 nar = ar - 1
#                 nac = ac + 1
#             elif ar < jr and ac < jc:
#                 nar = ar + 1
#                 nac = ac + 1
#             else:
#                 nar = ar + 1
#                 nac = ac - 1
#         board[ar][ac] = '.'
#         bomb[ar][ac] -= 1
#         bomb[nar][nac] += 1
#         new_ard.add((nar, nac))
        
#     for i in range(R):
#         for j in range(C):
#             if bomb[i][j] == 1:
#                 if board[i][j] == 'I':
#                     return False
#                 board[i][j] = 'R'
#             elif bomb[i][j] > 1:
#                 bomb[i][j] = 0
#                 new_ard.remove((i, j))
                
                
#     arduinos = new_ard
#     return True
    



# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]
# bomb = [[0] * C for _ in range(R)]
# command = input()
# turn = 0
# arduinos = []
# jr, jc = 0, 0
# for i in range(R):
#     for j in range(C):
#         if board[i][j] == 'I':
#             jr, jc = i, j
#         elif board[i][j] == 'R':
#             arduinos.append((i, j))
#             bomb[i][j] = 1

# for i in range(len(command)):
#     ans = move(jr, jc, command[i])
#     if not ans:
#         print(f'kraj {i+1}')
#         break
# else:
#     for row in board:
#         print(''.join(row))

# 방향 벡터 설정
# dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
# dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

# def move(r, c, direction):
#     global jr, jc, arduinos
#     nr = r + dr[direction-1]
#     nc = c + dc[direction-1]
    
#     # 플레이어 이동
#     board[r][c] = '.'
#     jr, jc = nr, nc
    
#     # 만약 이동한 위치에 아두이노가 있다면 게임 오버
#     if board[nr][nc] == 'R':
#         return False
#     board[nr][nc] = 'I'
    
#     # 새로운 아두이노 위치 계산
#     new_positions = {}
#     for ar, ac in arduinos:
#         board[ar][ac] = '.'
#         min_dist = float('inf')
#         target_r, target_c = ar, ac
#         for i in range(9):
#             next_r = ar + dr[i]
#             next_c = ac + dc[i]
#             if 0 <= next_r < R and 0 <= next_c < C:
#                 dist = abs(jr - next_r) + abs(jc - next_c)
#                 if dist < min_dist:
#                     min_dist = dist
#                     target_r, target_c = next_r, next_c

#         # 새로운 위치에 도착한 아두이노의 수를 기록
#         if (target_r, target_c) not in new_positions:
#             new_positions[(target_r, target_c)] = 0
#         new_positions[(target_r, target_c)] += 1
    
#     # 보드 초기화 및 아두이노 충돌 처리
#     arduinos.clear()
#     for (r, c), count in new_positions.items():
#         if count == 1:  # 해당 위치에 아두이노가 하나만 있다면
#             arduinos.append((r, c))
#             if (r, c) == (jr, jc):  # 아두이노가 플레이어 위치에 도달하면 게임 오버
#                 return False
#             board[r][c] = 'R'
#     return True

# # 입력 및 초기 설정
# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]
# command = list(map(int, input().strip()))

# arduinos = []
# jr, jc = 0, 0

# for i in range(R):
#     for j in range(C):
#         if board[i][j] == 'I':
#             jr, jc = i, j
#         elif board[i][j] == 'R':
#             arduinos.append((i, j))

# # 명령 처리
# for i, cmd in enumerate(command):
#     if not move(jr, jc, cmd):
#         print(f'kraj {i+1}')
#         break
# else:
#     for row in board:
#         print(''.join(row))

