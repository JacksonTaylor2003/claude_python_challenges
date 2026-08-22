def first_unique_char(s):
    unique_chars = set(s)
    dupe_chars = set()

    for char in unique_chars:
        if s.count(char) > 1:
            dupe_chars.add(char)

    unique_chars = unique_chars.difference(dupe_chars)

    for index, char in enumerate(s):
        if char in unique_chars:
            return index
    return -1

print(first_unique_char("leetcode"))     # 0   ('l' appears once, and it's first)
print(first_unique_char("loveleetcode")) # 2   ('v' is the first character with count 1)
print(first_unique_char("aabb"))         # -1  (every character repeats)