def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

print(selection_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
print(selection_sort([1]))                  # [1]
print(selection_sort([]))                   # []