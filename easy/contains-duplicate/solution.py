def containsDuplicate(nums: list[int]) -> bool:
    st = set()
    for num in nums:
        if num in st:
            return True
        else:
            st.add(num)
    return False
