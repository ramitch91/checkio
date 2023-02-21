def sum_digits(num: int) -> int:
    digits = [int(i) for i in str(num)]
    while sum(digits) > 9:
        sum_of_digits = sum(digits)
        digits = [int(i) for i in str(sum_of_digits)]
    return sum(digits)

print("Example:")
print(sum_digits(38))

assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
assert sum_digits(232) == 7
assert sum_digits(811) == 1
assert sum_digits(702) == 9

print("The mission is done! Click 'Check Solution' to earn rewards!")