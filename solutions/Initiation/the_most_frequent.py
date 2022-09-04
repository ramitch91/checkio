#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run the-most-frequent

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# It can be only one.
# 
# Input:non-empty list of strings.
# 
# Output:a string.
# 
# 
# END_DESC

def most_frequent(data: list[str]) -> str:
    # your code here
    counter = 0
    greatest = data[0]
    for item in data:
        current_count = data.count(item)
        if current_count > counter:
            counter = current_count
            greatest = item

    return greatest


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
