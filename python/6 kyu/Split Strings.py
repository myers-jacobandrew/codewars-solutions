def solution(s):
    list = []

    if len(s) % 2 != 0:
        s += "_"

    for i in range(0, len(s), 2):
        list.append(s[i : i + 2])
    return list
    
    pass