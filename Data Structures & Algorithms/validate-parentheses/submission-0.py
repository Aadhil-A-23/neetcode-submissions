class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]":"[", "}":"{", ")":"("}
        for v in s:
            if v not in pairs:
                stack.append(v)
            else:
                if not stack or stack.pop() != pairs[v]:
                    return False
        else:
            return len(stack) == 0