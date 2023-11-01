def move_zeros(lst):
    zeros = [z for z in lst if z in [0]]
    lst = [i for i in lst if i not in [0]]
    for _ in zeros:
        lst.append(0)
    return lst
