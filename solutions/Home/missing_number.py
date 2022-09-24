def missing_number(items: list[int]) -> int:
    # your code here
    sorted_items = sorted(items)
    list_diff = 100
    new_diff = 0
    for item in sorted_items:
        if sorted_items.index(item) == 0:
            continue
        new_diff = item - (sorted_items[sorted_items.index(item) - 1])
        if new_diff < list_diff:
            list_diff = new_diff

    for item in sorted_items:
        if item + new_diff != sorted_items[sorted_items.index(item) + 1]:
            return item + new_diff


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
