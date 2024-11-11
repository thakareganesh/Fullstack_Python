# Reverse Morse code dictionary (Morse code to text)
morse_to_text = {
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
    " ": "/",  # Space between words
    ".-.-.-": "."  # Full stop (period)
}

# Ask user for the Morse code input
morse_code_input = input("Type your Morse code (separate letters with spaces and words with '/'): ")

# Split the input Morse code by spaces to get individual codes
morse_code_list = morse_code_input.split(" ")

# Initialize output string
decoded_message = ""

# Convert each Morse code symbol to text
for code in morse_code_list:
    if code in morse_to_text:
        decoded_message += morse_to_text[code]
    else:
        decoded_message += "Invalid Morse Code / Unrecognized Morse Code"  # For unrecognized Morse code

# Print the decoded message
print(f"Your Decoded Message: {decoded_message}")
