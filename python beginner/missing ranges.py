nums = list(map(int, input().split()))
lower = int(input())
upper = int(input())

res = []

# Case 1: Empty array
if len(nums) == 0:
    res.append([lower, upper])

else:
    # Missing range before first element
    if nums[0] > lower:
        res.append([lower, nums[0] - 1])

    # Missing ranges between elements
    for i in range(1, len(nums)):
        if nums[i - 1] + 1 != nums[i]:
            res.append([nums[i - 1] + 1, nums[i] - 1])

    # Missing range after last element
    if nums[-1] < upper:
        res.append([nums[-1] + 1, upper])

print(res)