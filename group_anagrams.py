def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        sorted_word = tuple(sorted(word.lower()))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [word]
        else:
            anagram_dict[sorted_word].append(word)
    return list(anagram_dict.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))