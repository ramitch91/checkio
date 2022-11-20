"""
Sofia has had a very stressful month and decided to take a vacation for a week. To avoid any stress during her vacation
she wants to forward emails with a stressful subject line to Stephen.

The function should recognize if a subject line is stressful. A stressful subject line means that all letters are in
uppercase, and/or the whole line ends by at least 3 exclamation marks, and/or contains at least one of the following
“red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help",
"HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters
interspersed between them.

Input: Subject line as a string.

Output: Boolean.

Examples:

assert is_stressful("Hi") == False
assert is_stressful("I neeed HELP") == True
assert is_stressful("I neeed HLEP") == False

Precondition:
Subject can be up to 100 letters
"""


def is_stressful(subj):
    """
        recognize stressful subject
    """
    stressful = ["help", "asap", "urgent"]
    if subj.isupper():
        return True
    if subj[-3:] == "!!!":
        return True
    words = subj.split()
    for word in words:
        if len(word) < 3:
            continue
        if word.lower() in stressful:
            return True
        test_stressful = []
        for i in range(len(word)):
            if word[i].isalpha():
                if word[i] == word[i - 1]:
                    continue
                test_stressful.append(word[i].lower())
            else:
                continue
        test_word = "".join(test_stressful)
        if test_word in stressful:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I need h!e!l!p") == True, "Third"
    assert is_stressful("Thsi is u-r-g-e-n-t") == True, "Fourth"
    assert is_stressful("Please hhheeeeeeeeeellllllppp") == True, "Fifth"
    assert is_stressful("Have a nice weekend") == False, "Sixth"
    print('Done! Go Check it!')
