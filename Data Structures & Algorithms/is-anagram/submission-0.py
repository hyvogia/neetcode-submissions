class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sarr = {}
        tarr = {}

        for i in range(len(s)):
            sarr[s[i]] = 1 + sarr.get(s[i],0)
            tarr[t[i]] = 1 + tarr.get(t[i],0)
        return sarr == tarr              