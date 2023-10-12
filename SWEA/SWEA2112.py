# 보호 필름
# 검사 알고리즘
def check(D, W, K):
    
    for c in range(W):
        flag = 0
        for r in range(D-1):
            if film[r][c] == film[r+1][c]:
                flag += 1
            else:
                flag = 0
            if flag == K-1:
                break
        if flag != K-1:
            return False
    return True

def dfs(level, start, film):
    global ans
    # 기존의 최솟값을 level(약품을 투여한 층의 갯수)이 초과하면 할 필요없다.(가지치기)
    if level >= ans:
        return
    
    # 성능 검사
    if check(D, W, K): 
        # level(약품 투입 층의 갯수)이 ans보다 적으면 갱신
        if level < ans:
            ans = level
        return
    
    # 합격 기준만큼 A 혹은 B로 연속으로 투입하면 합격할 수 밖에 없으므로 level이 K와 같아졌을 때를 기준으로 잡는다.
    if level == K:
        if level < ans:
            ans = level
        return
    else:
        # 조합 알고리즘 응용
        for r in range(start, D):
            changed_cell = []

            # A 약품 투입 과정
            for c in range(W):
                if film[r][c] == 1: 
                    film[r][c] = 0
                    changed_cell.append(c) # 바뀐 셀 위치 인덱스를 저장해놓는다
            dfs(level+1, r+1, film)
            
            # 약품 바른거 되돌리기
            for cell in changed_cell:
                film[r][cell] = 1 
            
            # 초기화
            changed_cell = []

            for c in range(W):
                if film[r][c] == 0:
                    film[r][c] = 1
                    changed_cell.append(c)
            dfs(level+1, r+1, film)
            
            # 약품 바른거 되돌리기
            for cell in changed_cell:
                film[r][cell] = 0

T = int(input())    
for tc in range(1, 1+T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    if K == 1:
        print(f'#{tc} {0}')
    else:
        dfs(0, 0, film)
        print(f'#{tc} {ans}')