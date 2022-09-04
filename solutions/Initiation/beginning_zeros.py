#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run beginning-zeros

# You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
# 
# Input:A string, that consist of digits.
# 
# Output:An Int.
# 
# Precondition:0-9
# 
# 
# END_DESC

def beginning_zeros(a: str) -> int:
    # your code here
    return None

print('Example:')
print(beginning_zeros('10'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")