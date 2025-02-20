class Solution:

    # this is cheating
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         ans = haystack.index(needle)
    #     except:
    #         ans = -1
    #     return ans
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1