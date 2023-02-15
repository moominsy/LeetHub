class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(", "}":"{", "]":"["}
        for n in s:
            if n in d: # n is closing bracket
                if len(stack) == 0:
                    return False
                if d[n] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(n)
        if len(stack) == 0:
            return True
        else:
            return False

            