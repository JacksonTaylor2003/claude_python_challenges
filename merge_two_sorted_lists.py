def merge_sorted(list1, list2):
    index1 = 0
    index2 = 0
    merged = []

    while index1 < len(list1) and index2 < len(list2):

        if list1[index1] < list2[index2]:
            merged.append(list1[index1])
            index1 += 1
        else:
            merged.append(list2[index2])
            index2 += 1

    if index1 == len(list1):
        merged += list2[index2:]
    elif index2 == len(list2):
        merged += list1[index1:]

    return merged


print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
print(merge_sorted([1, 2, 3], []))          # [1, 2, 3]
print(merge_sorted([], []))                 # []
print(merge_sorted([5, 10], [1, 2, 3]))     # [1, 2, 3, 5, 10]
