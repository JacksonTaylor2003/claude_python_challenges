def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

        

binary_search([1, 3, 5, 7, 9, 11], 7)    # 3
binary_search([1, 3, 5, 7, 9, 11], 4)    # -1
binary_search([2, 4, 6, 8], 2)           # 0
binary_search([], 5)                     # -1