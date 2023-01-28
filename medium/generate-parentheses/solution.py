def generateParenthesis(n: int) -> list[str]:
    # * = (*) | *() | ()*
    # n = 1: ()
    # n = 2: (()) | ()()
    # n = 3: ((())) | (())() | ()(()) || (()()) | ()()()
    if n == 0:
        return [""]
    result = []
    st = set()
    for pair in generateParenthesis(n - 1):
        pair1 = '(' + pair + ')'
        if pair1 not in st:
            st.add(pair1)
            result.append(pair1)
        pair2 = pair + '()'
        if pair2 not in st:
            st.add(pair2)
            result.append(pair2)
        pair3 = '()' + pair
        if pair3 not in st:
            st.add(pair3)
            result.append(pair3)
    return result


print(generateParenthesis(3))
