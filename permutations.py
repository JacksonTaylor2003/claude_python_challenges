def permutations(s):
    permutation_list = []
    if len(s) < 2:
        permutation_list.append(s)
        return permutation_list
    for index, value in enumerate(s):
        first_char = value
        for string in permutations(s[:index]+s[index+1:]):
            permutation_list.append(first_char+string)

    return permutation_list