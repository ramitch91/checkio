#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run morse-decoder

# Your task is to decrypt the secret message using theMorse code.
# The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
# 
# 
# 
# Input:The secret message (string).
# 
# Output:The decrypted text (string).
# 
# Precondition:
# 0 < len(message) < 100
# The message will consist of numbers and English letters only.
# 
# 
# END_DESC

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    # replace this for solution

    # Split the morse code into words
    words = code.split("   ")
    new_code = []
    for word in words:
        new_letters = []
        # Split the word into letters
        letters = word.split(" ")

        # Cycle through the letters to see what they are
        for letter in letters:
            new_letters.append(MORSE.get(letter))

        new_word = ''.join(new_letters)
        new_code.append(new_word)

    # Check if first character is a letter and if so capitalize it
    try:
        int(new_code[0][0])
    except ValueError:
        new_code[0] = new_code[0].capitalize()

    # Join the new_code list back into one readable code
    final_code = " ".join(new_code)
    print(final_code)

    return final_code


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
     morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
