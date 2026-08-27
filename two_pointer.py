def two_sum_sorted(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

print(two_sum_sorted([1, 2, 4, 6, 10], 8))    # [1, 3]   (2+6=8)
print(two_sum_sorted([2, 7, 11, 15], 9))      # [0, 1]   (2+7=9)