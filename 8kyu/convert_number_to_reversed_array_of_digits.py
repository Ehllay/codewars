def digitize(n):
    digits = [int(num) for num in str(n)]
    return digits[::-1]
