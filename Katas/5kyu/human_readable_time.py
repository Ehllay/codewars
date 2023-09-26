def make_readable(seconds):
    if 359999 >= seconds >= 0:
        h = str(seconds // 3600).zfill(2)
        m = str(seconds % 3600 // 60).zfill(2)
        s = str(seconds % 3600 % 60).zfill(2)
        return f"{h}:{m}:{s}"


print(make_readable(0))
