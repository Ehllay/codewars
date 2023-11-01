from math import sqrt


def find_next_square(sq):
    root = sqrt(sq)
    if root.is_integer():
        return (root + 1) ** 2
    else:
        return -1
