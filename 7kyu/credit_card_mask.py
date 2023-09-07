def maskify(cc):
    masked = ""
    for _ in str(cc)[:-4]:
        masked += "#"
        masked += cc[-4:]
    return masked
