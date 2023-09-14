def first_non_repeating_letter(s):
    result = s
    print(s.lower())
    for char in s.lower():
        if s.lower().count(char) != 1:
            result = result.replace(char.lower(), "").replace(char.upper(), "")
    if result:
        print(result)
        return result[0]
    else:
        return ""
