def is_opposite(s1, s2):
    # your code here
    result = ""
    if s1 or s2:
        for char in s1:
            if char.isupper():
                print(char)
                result = result + char.lower()
            elif char.islower():
                result = result + char.upper()
        if result == s2:
            print(result)
            return True
        else:
            return False
    else:
        return False
