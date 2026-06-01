class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        storage = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in storage:
                if stack and stack[-1] == storage[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
