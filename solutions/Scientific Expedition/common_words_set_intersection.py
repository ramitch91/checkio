"""
 Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common
 between these strings. The words in the same string don't repeat.

Your function should find all the words that appear in both strings. The result must be represented as a string of
words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.

Example:
assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful for linguistic
analysis.

Precondition:
Each string contains no more than 10 words.
All words separated by commas.
All words consist of lowercase latin letters.
"""


def checkio(line1: str, line2: str) -> str:
    common_words = []
    a = set(line1.split(","))
    b = set(line2.split(","))
    common_words = list(a & b)
    common_words.sort()
    return ",".join(common_words)


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
