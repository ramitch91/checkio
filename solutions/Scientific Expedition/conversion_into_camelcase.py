"""
Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name")
into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated
without any intervening characters.

Input: A function name as a string.

Output: The same string, but in CamelCase.

Example:
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"
1
2

How it is used: To apply function names in the style in which they are adopted in a specific language (Python,
JavaScript, etc.).

Precondition :
0 < len(string) <= 100
Input data won't contain any numbers.
"""


def to_camel_case(name: str) -> str:
    items = name.split("_")
    word_list = []
    for item in items:
        for character in item:
            if character == item[0]:
                word_list.append(character.upper())
                continue
            word_list.append(character)
    return "".join(word_list)


print("Example:")
print(to_camel_case("my_function_name"))

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
