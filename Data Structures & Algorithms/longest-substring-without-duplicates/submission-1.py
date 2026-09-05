class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            m = max(m, right - left + 1)
        return m