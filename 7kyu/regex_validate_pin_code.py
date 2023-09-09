import re


def validate_pin(pin):
    search = re.search(r"(?:^\d{6}$|^\d{4}$)", pin)

    if "\n" in pin:
        return False
    elif search:
        return True
    else:
        return False
