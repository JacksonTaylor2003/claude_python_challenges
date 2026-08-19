def two_sum(nums, target):
    num_dict = {}
    
    for index, number in enumerate(nums):
        complement = (target - number)

        if complement in num_dict:
            return [num_dict[complement], index]
        else:
            num_dict[number] = index


            

print(two_sum([2, 7, 11, 15], 9))    # [0, 1]   (2 + 7 = 9)
print(two_sum([3, 2, 4], 6))         # [1, 2]   (2 + 4 = 6)
print(two_sum([3, 3], 6))            # [0, 1]   (3 + 3 = 6)