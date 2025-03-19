class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sc = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in sc:
                while s[l] != s[r]: 
                    sc.remove(s[l])
                    l += 1
                sc.remove(s[l])
                l += 1
            sc.add(s[r])
            res = max(res, r - l + 1)
        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         sc = set()
#         l = 0
#         res = 0
#         for r in range(len(s)):
#             while s[r] in sc:
#                 sc.remove(s[l])
#                 l += 1

#             sc.add(s[r])
#             res = max(res, r - l + 1)
#         return res