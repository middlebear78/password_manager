class Password:
    SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    def __init__(self):
        self.password_elements = []
        self.generated_password = ""

    def user_set_password(self):
        self.password = input("Please Enter a password with at least 8 characters\nwhich include 1 Uppercase, 1 Lowercase, and 1 number: ")
        return self.password

    def decide_params(self):
        from random import randint
        minimum_number = 1
        num_of_char = randint(10, 15)
        num_of_lowercase = randint(minimum_number, max(num_of_char - 3, minimum_number))
        num_of_uppercase = randint(minimum_number, max(num_of_char - num_of_lowercase - 2, minimum_number))
        num_of_numbers = randint(minimum_number, max(num_of_char - num_of_lowercase - num_of_uppercase - 1, minimum_number))
        num_of_symbols = num_of_char - (num_of_lowercase + num_of_uppercase + num_of_numbers)

        return [num_of_lowercase, num_of_uppercase, num_of_numbers, num_of_symbols]

    def generate_password(self, params):
        from random import randint, choice, shuffle
        char_types = [('a', 'z'), ('A', 'Z'), ('0', '9'), (None, None)]  # Symbol is handled separately
        for i, (start, end) in enumerate(char_types):
            if start and end:
                self.password_elements.extend([chr(randint(ord(start), ord(end))) for _ in range(params[i])])
            else:
                self.password_elements.extend([choice(self.SYMBOLS) for _ in range(params[i])])

        shuffle(self.password_elements)
        self.generated_password = ''.join(self.password_elements)
        return self.generated_password

    def check_password(self, password):
        if not password:
            raise ValueError("Password cannot be empty.")
        if len(password) < 8:
            raise ValueError("Password must be 8 characters or more.")
        
        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_number = any(char.isdigit() for char in password)
        if not has_lowercase:
            raise ValueError("Password must have at least 1 lowercase letter.")
        if not has_uppercase:
            raise ValueError("Password must have at least 1 upperca[?12;4$yse letter.")
        if not has_number:
            raise ValueError("Password must have at least 1 number.")

        return True

    def reset_password(self):
        # Placeholder for password reset functionality
        self.password_elements = []
        self.generated_password = ""

if __name__ == '__main__':
    try:
        password_manager = Password()
        params = password_manager.decide_params()
        generated_password = password_manager.generate_password(params)
        print(generated_password)

        if password_manager.check_password(generated_password):
            print("Generated password is valid.")
        
        user_password = password_manager.user_set_password()
        if password_manager.check_password(user_password):
            print("User-set password is valid.")

    except ValueError as ve:
        print(ve)
    except Exception as err:
        print(err)

