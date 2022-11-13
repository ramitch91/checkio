"""
You are given a list of integers. Your task in this mission is to find, how many times the sorting direction was
changed in the given list. If the elements are equal - the previous sorting direction remains the same, if the
sequence starts from the same elements - look for the next different to determine the sorting direction.

 There are three sorting directions:

    on the chunk 1, 2, 2 - up (increasing);
    on the chunk 2, 1 - down (decreasing);
    and on the chunk 1, 2, 2 - up again.

So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up. That's the
result your function should return.

Input: A list of integers.

Output: Integer.

Examples:
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
1
2
3

Precondition:

    the list is non-empty;
    the elements in the list are positive integers.

"""


def changing_direction(elements: list[int]) -> int:
    direction = "down"
    changes = []
    for i in range(len(elements)):
        if i == 0:
            direction = "up"
        if i > 0 and elements[i] > elements[i - 1]:
            direction = "up"
            changes.append(direction)
        elif i > 0 and elements[i] < elements[i - 1]:
            direction = "down"
            changes.append(direction)
    count = 0
    for i in range(len(changes)):
        if i > 0 and changes[i] != changes[i - 1]:
            count += 1
    return count


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
