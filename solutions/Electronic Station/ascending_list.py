#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run ascending-list

# Determine whether the list of elements is ascending such that each of its elements    is strictly larger than (and
# not merely equal to) the preceding element.    Empty list consider as ascending.
# 
# Input:List with ints.
# 
# Output:Bool.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education
# byIlkka Kokkarinen
# 
# 
# END_DESC

def is_ascending(items: list[int]) -> bool:
    if len(items) == 0:
        return True
    sorted_items = sorted(items)
    if sorted_items == items:
        new_items = []
        for item in items:
            if item not in new_items:
                new_items.append(item)
        if len(items) == len(new_items):
            return True
    return False


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")