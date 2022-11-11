"""
 In this mission you need to create a password verification function.

The verification conditions are:

   -the length should be bigger than 6;
   -should contain at least one digit, but it cannot consist of just digits;
   -having numbers or containing just numbers does not apply to the password
    longer than 9.
   -a string should not contain the word "password" in any case;
   -should contain at least 3 different letters (or digits) even if it is
    longer than 10

Input: A string.

Output: A bool.
"""


def count_different_characters(password: str) -> bool:
    diff_characters = []
    for character in password:
        if character not in diff_characters:
            diff_characters.append(character)
    if len(diff_characters) >= 3:
        return True
    return False


def is_acceptable_password(password: str) -> bool:
    if not count_different_characters(password):
        return False
    if "password" in password.lower():
        return False
    if len(password) > 9:
        return True
    if len(password) > 6:
        if any(char.isdigit() for char in password):
            if not password.isdigit():
                return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
