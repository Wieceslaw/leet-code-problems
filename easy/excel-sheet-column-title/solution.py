def convertToTitle(columnNumber: int) -> str:
    result = ""
    while columnNumber >= 26:
        n = columnNumber % 26
        result = chr(n + 65) + result
        columnNumber = columnNumber // 26
    result = chr(columnNumber + 65) + result
    return result


print(convertToTitle(52))
