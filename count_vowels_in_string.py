def count_vowels(s):
    if not s:
        return 0

    count = count_vowels(s[1:])

    if s[0] in "aeiou":
        return count + 1
    else:
        return count


print(count_vowels("hello"))