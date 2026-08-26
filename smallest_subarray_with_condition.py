def min_subarray_len(nums, target):
    start = 0
    current_sum = 0
    min_length = float("inf")

    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum >= target:
            if (end - start + 1) < min_length:
                min_length = (end - start + 1)
            current_sum -= nums[start]
            start += 1

    if min_length == float("inf"):
        return 0
    else:
        return min_length

min_subarray_len([2, 3, 1, 2, 4, 3], 7)
# 2   -> [4, 3] sums to 7, and it's the shortest subarray that reaches at least 7

min_subarray_len([1, 4, 4], 8)
# 2   -> [4, 4]

min_subarray_len([1, 1, 1, 1], 11)
# 0   -> no subarray sums to 11 or more, total is only 4