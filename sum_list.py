def sum_list(nums):
    if not nums:
        return 0
    last_element = nums[-1]
    rest = nums[0:-1]
    return last_element + sum_list(rest)

print(sum_list([1, 2, 3, 4]))