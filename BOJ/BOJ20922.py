# 겹치는 건 싫어

N, K = map(int, input().split())
nums = list(map(int, input().split()))
counter = [0] * (max(nums)+1)
left, right = 0, 0
ans = 0
while right < N:
    if counter[nums[right]] < K:
        counter[nums[right]] += 1
        right += 1
    else:
        counter[nums[left]] -= 1
        left += 1
    ans = max(ans, right-left)
print(ans)