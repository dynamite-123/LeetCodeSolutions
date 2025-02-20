class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            ans = haystack.index(needle)
        except:
            ans = -1
        return ans
