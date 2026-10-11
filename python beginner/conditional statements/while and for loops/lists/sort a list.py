nums = [5, 2, 9, 1, 7]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]   # swap

print("Sorted list:", nums)
