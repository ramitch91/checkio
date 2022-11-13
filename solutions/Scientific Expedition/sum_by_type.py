"""
You have a list. Each value from that list can be either a string or an integer. Your task here is to return two
values. The first one is a concatenation of all strings from the given list. The second one is a sum of all integers
from the given list.

Input: A list of strings and integers.

Output: A list or tuple.

Examples:
assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]

How it’s used: Input the values of different types and different operations with them, depending on type, is the usual
thing in development.
"""


def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    # your code here
    return ["", 0]


print("Example:")
print(list(sum_by_types([])))

assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]

print("The mission is done! Click 'Check Solution' to earn rewards!")