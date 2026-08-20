def find_duplicates(nums):
    seen_set = set()
    dupe_set = set()

    for num in nums:
        if num in seen_set:
            dupe_set.add(num)
        else:
            seen_set.add(num)

    return list(dupe_set)



find_duplicates([1, 2, 3, 2, 4, 5, 1])   # [2, 1]  (order = order they were confirmed as duplicates)
find_duplicates([1, 2, 3])               # []      (no duplicates)
find_duplicates([4, 4, 4, 4])            # [4]     (appears 4 times, but only listed once)