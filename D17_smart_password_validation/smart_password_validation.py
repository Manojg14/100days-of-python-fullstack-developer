
class BasicValidation:
    
    def all_lowercase(self, password):
        return password.islower()

    def common_word(self, password):
        return password.lower() in ["password", "admin", "test"]


class PasswordRules:
    
    def count_character_types(self, password):
        count_upper = count_lower = count_special_ch = count_number = 0

        for letter in password:
            if 'A' <= letter <= 'Z':
                count_upper += 1
            elif 'a' <= letter <= 'z':
                count_lower += 1
            elif letter in '!#@$%&*':
                count_special_ch += 1
            elif letter.isdigit():
                count_number += 1

        return count_upper, count_lower, count_special_ch, count_number


class PasswordChecker(BasicValidation, PasswordRules):
    
    def check_password(self, password):
        if self.all_lowercase(password) or self.common_word(password):
            print("Your password is invalid. Please enter at least 2 uppercase and lowercase, 2 digits with 2 symbols.")
            return

        count_upper, count_lower, count_special_ch, count_number = self.count_character_types(password)
        total = count_upper + count_lower + count_special_ch + count_number

        if total >= 8 and count_upper >= 1 and count_lower >= 3 and count_special_ch >= 1 and count_number >= 3:
            print("Valid Password")
        else:
            print("Invalid password,follow the password rules.")


class CheckPassword(PasswordChecker):
    
    def __init__(self):
        super().__init__()

ch_password = CheckPassword()

while True:
    user_input = input("Enter the password ('type' or 'exit'): ")
    if user_input.lower() == 'exit':
        print("process Exiting...")
        break
    ch_password.check_password(user_input)

