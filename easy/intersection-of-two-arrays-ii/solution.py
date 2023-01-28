def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    dct1 = {}
    dct2 = {}

    for el in nums1:
        if el in dct1:
            dct1[el] += 1
        else:
            dct1[el] = 1

    for el in nums2:
        if el in dct1:
            if el in dct2:
                if dct1[el] > dct2[el]:
                    dct2[el] += 1
            else:
                dct2[el] = 1

    result = []
    for key in dct2:
        result.extend([key] * dct2[key])
    return result


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
