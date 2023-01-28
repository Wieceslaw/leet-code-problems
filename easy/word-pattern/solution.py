def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    length = len(pattern)
    if length != len(words):
        return False

    dct = dict()
    for i in range(length):
        if pattern[i] not in dct:
            if words[i] in dct.values():
                return False
            dct[pattern[i]] = words[i]
        else:
            if dct[pattern[i]] != words[i]:
                return False
    return True
