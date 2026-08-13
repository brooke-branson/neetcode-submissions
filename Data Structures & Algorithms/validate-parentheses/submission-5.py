class Solution:
    def isValid(self, s: str) -> bool:
        valid = "()[]{}"
        stack = []
        balanced = True
        for x in s:
            if x in "{[(":
                stack.append(x)
            elif x in "]})":
                if not stack:
                    balanced = False
                    break
                top = stack.pop()
                if top + x not in valid:
                    balanced = False
                    break
        if stack:
            balanced = False
        return balanced