MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    "?": "..--..",
    "/": "-..-.",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def letters_to_morse_code(user_string):
    morse_translate = []
    for char in user_string.upper():
        morse_translate.append(MORSE_CODE.get(char))

    assert len(user_string) == len(morse_translate), (
        "The number of characters" "in input string and output string do not match."
    )

    assert user_string.count(" ") == morse_translate.count("/"), (
        "The number of spaces in" " input string and output string do not match."
    )

    return " ".join(morse_translate)


def morse_code_to_letters(user_string):
    if user_string == "":
        return user_string

    letter_translate = ""
    user_string = user_string.split(" ")
    for char in user_string:
        for key, value in MORSE_CODE.items():
            if value == char:
                letter_translate += key

    assert len(letter_translate) == len(user_string), (
        "The number of characters" " in input string and output string do not match."
    )

    assert letter_translate.count(" ") == user_string.count("/"), (
        "The number of" " spaces in input string and output string do not match."
    )

    return letter_translate
