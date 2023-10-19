# 별 찍기 - 10
import pprint
def star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    arr = star(n//3)
    big_star = []
    # 첫 번째 뭉탱이
    for i in arr:
        big_star.append(i*3)
    # 두 번째 뭉탱이
    for i in arr:
        big_star.append(i + ' '*(n//3) + i)
    # 세 번째 뭉탱이
    for i in arr:
        big_star.append(i*3)
    
    return big_star


n = int(input())
star(n)
for star in star(n):
    print(star)