from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # hamming distance = 1
        # adjacent indices is diff
        N = len(words)
        dp = {}
        def check(str1: str, str2: str) -> bool:
            if not str1 or not str2: 
                return True

            if len(str1) != len(str2):
                return False
            count = 0

            for s1, s2 in zip(str1, str2):
                if s1 != s2:
                    count += 1
            return count == 1

        res = []

        def helper(i: int, p: int, prev: str, cur: list) -> None:
            nonlocal res
            l = len(cur)

            if l > len(res):
                res = cur.copy()

            if i == N:
                return
            
            if i in dp and l <= dp[i]:
                helper(i + 1, p, prev, cur)
                return  

            if p != groups[i] and check(prev, words[i]):
                dp[i] = l
                helper(i + 1, groups[i], words[i], cur + [words[i]])
            helper(i + 1, p, prev, cur)

        helper(0, -1, "", [])

        return res


        