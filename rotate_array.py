def rotate_array(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
print(rotate_array(nums, 2))
# nums is now [4, 5, 1, 2, 3]

nums2 = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array(nums2, 3))
# nums2 is now [5, 6, 7, 1, 2, 3, 4]

nums3 = [1, 2]
print(rotate_array(nums3, 3))
# nums3 is now [2, 1]   (k can be larger than the list length)