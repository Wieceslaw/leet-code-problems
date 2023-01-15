def lengthOfLastWord(s: str) -> int:
    last_word_len = 0
    cur_word_len = 0

    for char in s:
        if char == " ":
            if cur_word_len:
                last_word_len = cur_word_len
            cur_word_len = 0
        else:
            cur_word_len += 1
    if cur_word_len:
        last_word_len = cur_word_len
    return last_word_len
