def longestPalindrome(s: str) -> int:
    dct = {}
    for el in s:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1

    one = 0
    result = 0
    for value in dct.values():
        part = value % 2
        if part:
            one = 1
            value -= 1
        result += value
    return result + one


print(longestPalindrome("aba"))
