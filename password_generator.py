import random
import string

class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.specials = string.punctuation

    def generate_password(self, length, numbers=True, special_characters=True):
        digits = self.digits
        specials = self.specials

        if numbers:
            while True:
                try:
                    start_digit = int(input("Starting from which number (Digits) :: "))
                    end_digit = int(input("To which number (Digits) :: "))
                    digits = digits[start_digit:end_digit+1]
                    break
                except ValueError as e:
                    print("Invalid input:", e)

        if special_characters:
            special_include = input("Enter special character you want to include: ")
            specials = special_include

        characters = self.letters
        if numbers:
            characters += digits
        if special_characters:
            characters += specials

        pwd = ""
        criteria = False
        has_number = False
        has_special = False

        while len(pwd) < length or not criteria:
            new_char = random.choice(characters)
            pwd += new_char

            if new_char in digits:
                has_number = True
            elif new_char in specials:
                has_special = True
            criteria = True
            if numbers:
                criteria = has_number
            if special_characters:
                criteria = criteria and has_special

        return pwd

if __name__ == "__main__":
    password_generator = PasswordGenerator()

    while True:
        try:
            length = int(input("Enter Length of Password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print("Invalid input:", e)

    while True:
        has_number_input = input("Do you want to have Numbers (y/n)? : ").lower()
        if has_number_input in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    has_number = has_number_input == "y"

    while True:
        has_special_input = input("Do you want to have Special characters (y/n)? : ").lower()
        if has_special_input in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    has_special = has_special_input == "y"

    pwd = password_generator.generate_password(length, has_number, has_special)
    print("Generated Password is :", pwd)
