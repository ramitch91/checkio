#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run split-pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters,
# then the missing second character of the final pair should be replaced with an underscore ('_').
# 
# Input:A string.
# 
# Output:A list or another Iterable of strings.
# 
# Precondition:0 <= len(text) <= 100
# 
# 
# END_DESC

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    split_text = []
    new_string = text
    if len(text) % 2 == 1:
        new_string = text + "_"
    while len(new_string):
        split_text.append(new_string[:2])
        new_string = new_string[2:]
    return split_text


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
