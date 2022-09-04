#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run max-digit

# You have a number, and you need to determine which digit in this number is the biggest.
# 
# Input:A positive int.
# 
# Output:An Int (0-9).
# 
# 
# END_DESC

def max_digit(a: int) -> int:
    # your code here
    max_num = 0
    num_string = str(a)
    for digit in num_string:
        if int(digit) > max_num:
            max_num = int(digit)
    return max_num


print('Example:')
print(max_digit(10))

assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
