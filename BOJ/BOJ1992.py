# 쿼드 트리
def quad(x, y, n):
    global res
    number = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 사분면에서 일치하지 않는 경우 발생
            if number != arr[i][j]:
                number = -1
    # 사분면 전체가 일치하지 않을 경우
    if number == -1:
        res += '('
        n = n // 2
        # 1~4 분면 다시 진행
        quad(x, y, n)
        quad(x, y+n, n)
        quad(x+n, y, n)
        quad(x+n, y+n, n)
        res += ')'
        
    # 사분면 전체가 일치하면 그 숫자 붙여넣으면 됨
    else:
        res += str(number)
        


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
res = ''
quad(0, 0, N)
print(res)