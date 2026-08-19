def count_occurrences(nums:list[int], target:int):

    if len(nums) == 0:
        return 0

    count = count_occurrences(nums[1:], target)

    if nums[0] == target:
        return count + 1
    else:
        return count
    


print(count_occurrences([1, 2, 3, 2, 2, 4], 2))