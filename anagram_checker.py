def are_anagrams(s1, s2):
    def build_freq_dict(s):
        freq_dict = {}
        for char in s.lower().replace(" ", ""):
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
        return freq_dict
    
    freq_dict1 = build_freq_dict(s1)
    freq_dict2 = build_freq_dict(s2)

    return freq_dict1 == freq_dict2

print(are_anagrams("listen", "silent"))           # True
print(are_anagrams("Dormitory", "Dirty Room"))    # True
print(are_anagrams("hello", "world"))             # False
print(are_anagrams("aabbcc", "abcabc"))           # True
print(are_anagrams("aabbcc", "aabbc"))            # False  <- different lengths/counts