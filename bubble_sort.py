def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            return nums
    return nums

print(bubble_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
print(bubble_sort([1]))                  # [1]
print(bubble_sort([]))                   # []