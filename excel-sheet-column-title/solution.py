def convertToTitle(columnNumber: int) -> str:
    columnNumber -= 1
    while columnNumber >= 26:
        n = columnNumber % 26
        print(n)
        columnNumber = columnNumber // 26
    print(columnNumber)

# print(chr(65 + 25))
convertToTitle(28)
