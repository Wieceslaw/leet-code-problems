def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    dct = {}
    mn = k + 1
    for i, num in enumerate(nums):
        if num not in dct:
            dct[num] = i
        else:
            mn = min(i - dct[num], mn)
            if mn <= k:
                return True
            dct[num] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
