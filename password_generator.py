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

def password_tool():

    def menu_input():
        while True:
            print("\033[H\033[J", end="")
            try:
                user_input = int(input("""1. Check password strength\n2. Generate a password\n3. Quit\n>>> """))
            except ValueError as e:
                user_input = None

            if user_input == 1:
                print(check_input())
                input("Press enter to continue...")
            elif user_input == 2:
                print(generate_input())
                input("Press enter to continue...")
            elif user_input == 3:
                print("Goodbye!")
                break
            else:
                continue
    def check_input():
        print("\033[H\033[J", end="")
        user_input = input("Please enter your password\n>>> ")
        return check_strength(user_input)
    def generate_input():
        while True:
            print("\033[H\033[J", end="")
            user_input = input("Please enter a password length >= 4\n>>> ")
            if user_input == "":
                return generate_password()
            else:
                try:
                    int(user_input)
                except ValueError as e:
                    continue 
                if int(user_input) < 4:
                    continue
                return generate_password(int(user_input))

    menu_input()

password_tool()