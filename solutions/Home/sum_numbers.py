#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run sum-numbers

# In a given text you need to sum the numbers while excluding any digits that form part of a word.
# 
# The text consists of numbers, spaces and letters from the English alphabet.
# 
# Input:A string.
# 
# Output:An int.
# 
# 
# END_DESC

def sum_numbers(text: str) -> int:
    # your code here
    res = [int(s) for s in text.split() if s.isdigit()]
    result =  sum(res)        
    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")