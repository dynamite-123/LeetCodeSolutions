class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        
        for i in range(len(s)):
            l = r = i

            while l > -1 and r < len(s) and s[l] == s[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res