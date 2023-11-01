def vampire_test(x, y):
    vn = x * y
    nstr = str(x) + str(y)

    if sorted(nstr) == sorted(str(vn)):
        return True

    return False
