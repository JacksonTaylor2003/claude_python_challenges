import string
def caesar_encrypt(text, shift):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    shifted = (lower[shift:] + lower[:shift]) + (upper[shift:] + upper[:shift])

    table = str.maketrans(lower + upper, shifted)
    print(text.translate(table))

caesar_encrypt("hello", 3)          # "khoor"
caesar_encrypt("Hello, World!", 3)  # "Khoor, Zruog!"
caesar_encrypt("xyz", 3)            # "abc"   <- wraps around
caesar_encrypt("hello", 0)          # "hello"