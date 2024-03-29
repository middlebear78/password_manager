
class Password:

    SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    def __init__(self):

        self.password_elements = []
        self.password = ""
        self.generated_password = ""



    def user_set_password(self):
        self.password = input("Please Enter a password with at least 8 chacters\nwhich include 1 Uppercase, 1 Lowercase and 1 number: ")
        return self.password




    def decide_params(self) -> list:

        import random
        minimum_number = 1
        num_of_char = random.randint(10, 15)
        num_of_lowercase = random.randint(minimum_number, max(num_of_char - 3, minimum_number))
        diff = num_of_char - num_of_lowercase
        num_of_uppercase = random.randint(minimum_number, max(diff, minimum_number))
        diff -= num_of_uppercase
        num_of_numbers = random.randint(minimum_number, max(diff, minimum_number))

        sum_of_characters_until_now = num_of_lowercase + num_of_uppercase + num_of_numbers

        if num_of_char > sum_of_characters_until_now:
            num_of_symbols = num_of_char - sum_of_characters_until_now
            return [num_of_lowercase, num_of_uppercase, num_of_numbers, num_of_symbols]

        else:
            return [num_of_lowercase, num_of_uppercase, num_of_numbers]



    def generate_password(self, params: list):

        if not params:
            raise ValueError("Parameters must be a list")
        for param in params:
            if not isinstance(param, int):
                raise ValueError("Every parameter must be a full number")

        import random
        if len(params) == 4:
            for i in range(0, params[0]):
                self.password_elements.append(chr(random.randint(ord("a"), ord("z"))))
            for i in range(0, params[1]):
                self.password_elements.append(chr(random.randint(ord("A"), ord("Z"))))
            for i in range(0, params[2]):
                self.password_elements.append(str(random.randint(0, 9)))
            for i in range(0, params[3]):
                    self.password_elements.append(random.choice(self.SYMBOLS))
        else:
            for i in range(0, params[0]):
                self.password_elements.append(chr(random.randint(ord("a"), ord("z"))))
            for i in range(0, params[1]):
                self.password_elements.append(chr(random.randint(ord("A"), ord("Z"))))
            for i in range(0, params[2]):
                self.password_elements.append(str(random.randint(0, 9)))

        random.shuffle(self.password_elements)
        for e in self.password_elements:
            self.generated_password += e

        return self.generated_password


    def check_password(self, password:str):

        if not password:
            raise ValueError("Password cannot be empty.")
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        if len(password) < 8:
            raise ValueError("password must be 8 character or more")


        has_lowercase = False
        has_uppercase = False
        has_number = False

        for char in password:
            if char.islower():
                has_lowercase = True
            elif char.isupper():
                has_uppercase = True
            elif char.isdigit():
                has_number = True

            if has_lowercase and has_uppercase and has_number:
                break

        if not has_lowercase:
            return "Password must have at least 1 Lowercase letter."
        elif not has_uppercase:
            return "Password must have at least 1 Uppercase letter."
        elif not has_number:
            return "Password must have at least 1 Number."

        return True


    def reset_password(self):
        pass





if __name__ == '__main__':

    try:
        password = Password()
        params = password.decide_params()
        passwd = password.generate_password(params)
        print(passwd)

        print(password.check_password(passwd))
        user_password = password.user_set_password()
        print(password.check_password(user_password))

    except ValueError as ve:
        print(ve)
    except Exception as err:
        print(err)








