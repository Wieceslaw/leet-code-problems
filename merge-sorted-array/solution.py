def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    array = [0] * (m + n)
    cur1 = 0
    cur2 = 0
    for i in range(m + n):
        if cur1 < m and cur2 < n:
            mn = min(nums1[cur1], nums2[cur2])
            if mn == nums1[cur1]:
                array[i] = nums1[cur1]
                cur1 += 1
            else:
                array[i] = nums2[cur2]
                cur2 += 1
        elif cur1 < m:
            array[i] = nums1[cur1]
            cur1 += 1
        else:
            array[i] = nums2[cur2]
            cur2 += 1
    for i in range(m + n):
        nums1[i] = array[i]
