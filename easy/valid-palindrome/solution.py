def isPalindrome(s: str) -> bool:
    new_string = ''.join([char for char in s.lower() if char.isalnum()])
    length = len(new_string)
    for i in range(length // 2):
        if new_string[i] != new_string[length - i - 1]:
            return False
    return True
