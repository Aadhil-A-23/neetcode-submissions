class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        d = {}
# For the first string "S"
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False

        for v in d:
            if d[v] != 0:
                return False

        return True
