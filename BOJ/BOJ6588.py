# 골드바흐의 추측
'''
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

while True:
    number = int(input())
    if not number:
        break
    else:
        a, b = 2, number-2
        while True:
            if a == 0  or b == 0:
                print("Goldbach's conjecture is wrong")
                break
            if is_prime(a) and is_prime(b):
                print(f'{number} = {a} + {b}')
                break
            else:
                a += 1
                b -= 1
'''
# 시간 초과 -> 매번 소수판정하는게 비효율적인듯 보인다

prime_number = [1] * 1000001
prime_number[0] = 0
prime_number[1] = 0
e = int(1000001 ** 0.5)
for i in range(2, e+1):
    if prime_number[i]:
        for j in range(i*i, 1000001, i):
            prime_number[j] = 0

while True:
    number = int(input())
    if not number:
        break
    else:
        a, b = 3, number-3
        while True:
            if a > b:
                print("Goldbach's conjecture is wrong")
                break
            if prime_number[a] and prime_number[b]:
                print(f'{number} = {a} + {b}')
                break
            else:
                a += 2
                b -= 2
