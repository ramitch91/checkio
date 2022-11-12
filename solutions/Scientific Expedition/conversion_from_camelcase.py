"""
Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format
("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore
symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.

Example:
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"
1
2

How it is used: To apply function names in the style in which they are adopted in a specific language (Python,
JavaScript, etc.).

Precondition :
0 < len(string) <= 100
Input data won't contain any numbers.
"""


def from_camel_case(name: str) -> str:
    name_list = []
    for character in name:
        if character == name[0]:
            name_list.append(character.lower())
            continue
        if character.isupper():
            name_list.append("_")
            name_list.append(character.lower())
            continue
        name_list.append(character)
    new_name = "".join(name_list)
    return new_name


print("Example:")
print(from_camel_case("MyFunctionName"))

assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
