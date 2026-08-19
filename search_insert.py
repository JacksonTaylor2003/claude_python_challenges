def search_insert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

    

print(search_insert([1, 3, 5, 6], 5))   # 2   (5 is already at index 2)
print(search_insert([1, 3, 5, 6], 2))   # 1   (2 would go between 1 and 3, at index 1)
print(search_insert([1, 3, 5, 6], 7))   # 4   (7 is bigger than everything, goes at the end)
print(search_insert([1, 3, 5, 6], 0))   # 0   (0 is smaller than everything, goes at the start)