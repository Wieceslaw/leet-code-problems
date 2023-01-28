def reverseString(s: list[str]) -> None:
    length = len(s)
    for i in range(length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]


array = ["h", "e", "l", "l", "o"]
reverseString(array)
print(array)
