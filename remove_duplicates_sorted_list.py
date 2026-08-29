def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1 

nums = [1, 1, 2, 2, 3, 4, 4, 5]
k = remove_duplicates(nums)
print(k)
# k == 5
# nums[:k] == [1, 2, 3, 4, 5]   (the rest of nums beyond index 5 is irrelevant)

nums2 = [1, 1, 1]
k = remove_duplicates(nums2)
print(k)
# k == 1
# nums2[:k] == [1]