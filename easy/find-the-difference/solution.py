def findTheDifference(s: str, t: str) -> str:
    dct = {}
    for el in s:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1
    for el in t:
        if el not in dct:
            return el
        else:
            if dct[el] <= 0:
                return el
            else:
                dct[el] -= 1
