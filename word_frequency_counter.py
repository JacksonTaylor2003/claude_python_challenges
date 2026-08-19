import string
def word_frequency(text, top_n=None):
    word_dict = {}
    raw_text = text.lower()
    punctuation = string.punctuation

    for char in punctuation:
        if char in raw_text:
            raw_text = raw_text.replace(char, "")

    raw_text_list = raw_text.split()

    for word in raw_text_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    word_dict = sorted(word_dict.items(), key=lambda items: items[1], reverse=True)

    if top_n != None:
        return dict(word_dict[0:top_n])

    return dict(word_dict)



print(word_frequency("The quick brown. fox 'jumps' over the lazy dog. The dog barks!", 3))
    


