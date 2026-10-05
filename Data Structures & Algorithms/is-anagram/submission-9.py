class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = list(s)
        seen_t = list(t)
        seen_s.sort()
        seen_t.sort()
        for i in range(len(s)):
            if seen_s[i] != seen_t[i]:
                return False
        return True