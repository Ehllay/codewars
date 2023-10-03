from preloaded import MORSE_CODE


def decode_morse(morse_code):
    result = ""
    for i in morse_code.split(" "):
        if i == "":
            result += " "
        else:
            result += MORSE_CODE[i]

    return result.replace("  ", " ").strip()
