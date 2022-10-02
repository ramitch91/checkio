#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run the-most-frequent

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# It can be only one.
#
# Input:non-empty list of strings.
#
# Output:a string.
#
#
# END_DESC

from collections import Counter


def most_frequent(data: list[str]) -> str:
    # your code here
    data.sort(key=Counter(data).get, reverse=True)
    greatest = data[0]
    return greatest


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
