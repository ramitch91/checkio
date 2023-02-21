from typing import Iterable


def replace_last(line: list) -> Iterable:
    if len(line) < 2:
        return line
    else:
        temp = line[-1]
        for i in range(len(line) - 1, -1, -1):
            line[i] = line[i - 1]
        line[0] = temp
        return line


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
