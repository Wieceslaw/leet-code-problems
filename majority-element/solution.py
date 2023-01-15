def majorityElement(nums: list[int]) -> int:
    dct = dict()
    for num in nums:
        if num not in dct:
            dct[num] = 1
        else:
            dct[num] += 1
    return max(dct.keys(), key=lambda x: dct[x])


print(majorityElement([1, 2, 2, 2, 1, 1, 1, 1]))
