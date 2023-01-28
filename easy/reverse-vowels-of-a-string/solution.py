def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    length = len(s)
    l_ptr = 0
    r_ptr = length - 1
    new = list(s)
    while l_ptr < r_ptr:
        while l_ptr < length and not s[l_ptr] in vowels:
            l_ptr += 1
        while r_ptr >= 0 and not s[r_ptr] in vowels:
            r_ptr -= 1
        if l_ptr < r_ptr:
            new[r_ptr], new[l_ptr] = new[l_ptr], new[r_ptr]
            l_ptr += 1
            r_ptr -= 1
    return ''.join(new)


print(reverseVowels("leetcode"))
