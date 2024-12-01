# Morse code symbols dictionary
symbols = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/"  # Adding a separator for spaces between words
}

# Ask user for input
ask = input("Type your message in normal form: ").lower()

# Initialize output string
output = ""

# Convert each character to Morse code
for char in ask:
    if char in symbols:
        output += symbols[char] + " "
    else:
        output += "?"  # For invalid characters

# Print the encrypted message
print(f"Your Message in Encrypted Morse Code Form: {output}")
