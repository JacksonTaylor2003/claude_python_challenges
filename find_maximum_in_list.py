def find_max(nums):
    if len(nums) == 1:
        return nums[0]
    current_max = find_max(nums[1:])
    if nums[0] > current_max:
        return nums[0]
    else:
        return current_max



print(find_max([3, 7, 2, 9, 4]))   # 9
print(find_max([5]))               # 5
print(find_max([-1, -8, -3]))      # -1)


