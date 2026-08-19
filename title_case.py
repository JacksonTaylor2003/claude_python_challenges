def title_case(sentence, minor_words):
    new_sentence = sentence.split()

    for index, word in enumerate(new_sentence):
        if index == 0 or word not in minor_words:
            new_sentence[index] = word.capitalize()

    return(" ".join(new_sentence))


minor_words = ["a", "the", "of", "and", "in", "on"]
title_case("the lord of the rings", minor_words)
title_case("war and peace", minor_words)
title_case("a tale of two cities", minor_words)

