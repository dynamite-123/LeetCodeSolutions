from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        N = len(digits)
        mp = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }

        res = []

        def helper(i, cur):
            if i == N:
                res.append(cur)
                return
            for ch in mp[digits[i]]:
                helper(i + 1, cur + ch)

        helper(0, '')

        return res