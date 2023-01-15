def isIsomorphic(s: str, t: str) -> bool:
    table = dict()
    for i, char in enumerate(s):
        if char in table:
            if table[char] != t[i]:
                return False
        else:
            if t[i] in table.values():
                return False
            table[char] = t[i]
    return True


print(isIsomorphic("abb", "egg"))
