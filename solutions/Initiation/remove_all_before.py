#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run remove-all-before

# Not all the elements are important. What you need to do here is to remove from the list all the
# elements before the given one.
# 
# 
# 
# For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 -
# which is 1 and 2.
# 
# We have two edge cases here:
# (1) if a cutting element cannot be found, then the list shouldn't be changed.
# (2) if the list is empty, then it should remain empty.
# 
# Input:List and the border element.
# 
# Output:Iterable (tuple, list, iterator ...).
# 
# 
# END_DESC

from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    if border in items:
        border_index = items.index(border)
        items = items[border_index:]
    return items


print('Example:')
print(remove_all_before([1, 2, 3, 4, 5], 3))

assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
assert remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]
assert remove_all_before([], 0) == []
assert remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

print("The mission is done! Click 'Check Solution' to earn rewards!")
