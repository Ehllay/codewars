import re


def to_camel_case(text):
    ls = re.split("-|_", text)
    return "".join([w if w == ls[0] else w.title() for w in ls])
