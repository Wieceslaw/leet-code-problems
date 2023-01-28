def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False

    dct1 = {}
    for i, el in enumerate(t):
        if el in dct1:
            dct1[el].append(i)
        else:
            dct1[el] = [i]
    if s[0] not in dct1:
        return False
    for i in range(len(dct1[s[0]])):
        dct2 = {s[0]: i}
        start = dct1[s[0]][i]
        success = True
        last = start
        for j in range(1, len(s)):
            if s[j] not in dct1:
                success = False
                break
            else:
                if s[j] in dct2:
                    # find first char, which index > start and index > prev
                    flag = False
                    for index in dct1[s[j]][dct2[s[j]]:]:
                        if index > start and index > last:
                            last = index
                            flag = True
                            break
                    if not flag:
                        success = False
                        break
                    else:
                        dct2[s[j]] += 1
                else:
                    # find first char, which index > start
                    flag = False
                    for index in dct1[s[j]]:
                        if index > start and index > last:
                            last = index
                            flag = True
                            break
                    if not flag:
                        success = False
                        break
                    else:
                        dct2[s[j]] = 1
        if success:
            return True
        print(dct2)
    return False


s1 = "leeeeetcode"
s2 = "yyyyylyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeeeetcode"
print(isSubsequence(s1, s2))
