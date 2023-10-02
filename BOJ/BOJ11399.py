# ATM
n = int(input())
people = list(map(int, input().split()))
people.sort()

l = len(people)
ans = 0
for i in range(l):
    ans += people[i] * (l - i)

print(ans)