def firstUniqChar(s: str) -> int:
    dct = {}
    ignored = set()
    for i, char in enumerate(s):
        if char in ignored:
            continue
        if char in dct:
            ignored.add(char)
            dct.pop(char)
        else:
            dct[char] = i
    if not dct:
        return -1
    return min(dct.values())


print(firstUniqChar("aabb"))
