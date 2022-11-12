"""
You are given a text, which contains different English letters and punctuation symbols. You should find the most
frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency , then return the letter which comes first in the Latin
alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.
"""

from collections import Counter


def checkio(text: str) -> str:
    text_list = []
    for i in text:
        if not i.isalpha():
            continue
        else:
            text_list.append(i.lower())
            text_list.sort()
    occurrence_count = Counter(text_list)
    return occurrence_count.most_common(1)[0][0]
    # (1) - the most common item, [0] the first tuple of the most common items, [0] first element in the tuple


print("Example:")
print(checkio("Hello World!"))

assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
