import string
import secrets



class Password:

    def __init__(self):
        self.password = ''

    def user_set_password(self):

        while True:
            self.password = input("Please Enter a password with at least 8 chacters\nwhich include 1 Uppercase, 1 Lowercase, 1 number\nand 1 special character (!@#$..): ")
            if self.check_password(self.password):
                return self.password
            else:
                print("Password does not meet the needed requirements, please Try again.")


    def generate_password(self):

        characters = string.ascii_letters + string.digits + string.punctuation
        length = secrets.choice(range(8,13))
        self.password = "".join(secrets.choice(characters) for i in range(length))
        return self.password



    def check_password(self, password:str):

        conditions = [
            any(i.isupper() for i in password),
            any(i.islower() for i in password),
            any(i.isdigit() for i in password),
            any(i in string.punctuation for i in password)
        ]

        return all(conditions)

    def reset_password(self):
        self.password=''





if __name__ == '__main__':

    try:
        password = Password()
        passwd = password.generate_password()
        print(passwd)

        print(password.check_password(passwd))
        user_password = password.user_set_password()
        print(password.check_password(user_password))

    except ValueError as ve:
        print(ve)
    except Exception as err:
        print(err)

