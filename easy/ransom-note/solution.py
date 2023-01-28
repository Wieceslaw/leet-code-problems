def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    dct = {}
    for char in magazine:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1
    for char in ransomNote:
        if char not in dct:
            return False
        else:
            if dct[char] <= 0:
                return False
            else:
                dct[char] -= 1
    return True
