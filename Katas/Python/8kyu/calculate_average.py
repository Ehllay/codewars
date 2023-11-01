from statistics import mean


def find_average(numbers):
    if not numbers:
        return 0
    return mean(numbers)
