def max_sum_subarray(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum -= nums[i-k]
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
# 9   (the window [5, 1, 3] sums to 9, which is the largest of any 3 consecutive elements)

max_sum_subarray([1, 2, 3, 4, 5], 2)
# 9   ([4, 5])

max_sum_subarray([5, 5, 5, 5], 2)
# 10