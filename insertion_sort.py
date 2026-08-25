def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        position = i - 1
        while position >= 0 and nums[position] > current:
            nums[position+1] = nums[position]
            position -= 1
        nums[position+1] = current
    return nums

insertion_sort([5, 2, 8, 1, 9, 3])   # [1, 2, 3, 5, 8, 9]
insertion_sort([1])                  # [1]
insertion_sort([])                   # []