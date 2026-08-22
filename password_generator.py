import string
import random

def check_strength(password):
    points = []

    points.append(len(password) >= 8)
    points.append(any([char.isupper() for char in password]))
    points.append(any([char.islower() for char in password]))
    points.append(any([char.isdigit() for char in password]))
    points.append(any(char in string.punctuation for char in password))

    point_sum = sum(points)

    if point_sum <= 2:
        return "Weak"
    elif point_sum >= 3 and point_sum <= 4:
        return "Medium"
    else:
        return "Strong"

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):

    char_pool = ""
    guaranteed = []
    categories = [
        (use_upper, string.ascii_uppercase),
        (use_lower, string.ascii_lowercase),
        (use_digits, string.digits),
        (use_special, string.punctuation)
    ]

    for key, value in categories:
        if key:
            char_pool += value
            guaranteed.append(random.choice(value))
            length -= 1

    rest = random.choices(char_pool, k=length)

    password = guaranteed + rest

    random.shuffle(password)

    return "".join(password)

print(generate_password())