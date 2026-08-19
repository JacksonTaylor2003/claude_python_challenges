from string import punctuation

def longest_words(sentence):
    punctuation_table = str.maketrans("", "", punctuation)
    sentence.translate(punctuation_table)

    words = sentence.split()
    max_length = len(max(words, key=len))
    longest = [word for word in words if len(word) == max_length]

    return longest


longest_words("The quick brown fox jumps over the lazy dog")
# ["quick", "brown"]   <- both are 5 letters, the longest in the sentence

longest_words("I love programming in Python")
# ["programming"]

longest_words("A cat sat on a mat")
# ["cat", "sat", "mat"]  <- three-way tie