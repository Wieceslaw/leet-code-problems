def lengthOfLongestSubstring(s: str) -> int:
    dct = {}
    mx = 0
    count = 0
    for i, char in enumerate(s):
        if char not in dct:
            dct[char] = i
            count += 1
        else:
            if dct[char] >= (i - count):
                mx = max(count, mx)
                count -= dct[char]
                count = i - dct[char]
                dct[char] = i
            else:
                dct[char] = i
                count += 1
    mx = max(count, mx)
    return mx
