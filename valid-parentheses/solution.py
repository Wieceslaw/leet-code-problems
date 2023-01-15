def isValid(s: str) -> bool:
    stack = []
    for el in s:
        if el in "[({":
            stack.append(el)
        if el in "])}":
            if not stack:
                return False
            if el == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            elif el == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif el == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
    return not stack
