#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run first-word

# I might see a simplified version of this mission alreadyFirst Word (simplified). This mission is a little bit more complex as not only English letters can be in the given string.
# 
# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, one/multiple dot(s) or space(s).A word can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's it.Input:A string.
# 
# Output:A string.
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    translation = {44: 32, 46: 32}
    new = text.translate(translation)
    ans = new.split(' ')
    count = 0
    for i in range(len(ans)):
        if ans[i].isalpha() or "'" in ans[i]:
            count = i
            break
    return ans[count]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")