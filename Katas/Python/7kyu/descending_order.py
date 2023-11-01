def descending_order(num):
    return int("".join(sorted([d for d in str(num)], reverse=True)))
