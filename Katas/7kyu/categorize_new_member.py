def open_or_senior(data):
    return ["Senior" if p[0] >= 55 and p[1] > 7 else "Open" for p in data]
