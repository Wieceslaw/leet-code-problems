def isAnagram(s: str, t: str) -> bool:
    dct = dict()
    for char in s:
        if char not in dct:
            dct[char] = 1
        else:
            dct[char] += 1
    for char in t:
        if char not in dct:
            return False
        dct[char] -= 1
        if dct[char] < 0:
            return False
    for key in dct.keys():
        if dct[key] != 0:
            return False
    return True
