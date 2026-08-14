class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        balanced = True

        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in "}])":
                if not stack:
                    balanced = False
                    break
                top = stack.pop()
                if top + i not in "{}()[]":
                    balanced = False
                    break

        return balanced and not stack