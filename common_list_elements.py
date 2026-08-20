def common_elements(list1, list2):
    return list(set(list1) & set(list2))
    
common_elements([1, 2, 3, 4], [3, 4, 5, 6])       # [3, 4]
common_elements([1, 2, 3], [4, 5, 6])             # []
common_elements(["a", "b", "c"], ["b", "c", "d"]) # ["b", "c"]
common_elements([1, 1, 2], [1, 2, 2])             # [1, 2]  <- no duplicates even though inputs have them