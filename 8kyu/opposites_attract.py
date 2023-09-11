def lovefunc(flower1, flower2):
    if flower1 % 2 == 0:
        if flower2 % 2 != 0:
            return True

    elif flower1 % 2 != 0:
        if flower2 % 2 == 0:
            return True

    return False
