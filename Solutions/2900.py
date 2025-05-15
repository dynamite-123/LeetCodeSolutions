from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # recursive approach

        N = len(words)
        mx = 0

        res = []
        cur = []

        def helper(i, cur, prev):
            nonlocal mx, res
            if i >= N:
                if len(cur) > mx:
                    res = cur.copy()
                    mx = len(cur)
                return
            
            if groups[i] != prev:
                cur.append(words[i])
                helper(i + 1, cur, prev ^ 1)
                cur.pop() # should be added if cur.clear() is not present
            else:
                helper(i + 1, cur, prev)
            
        helper(0, cur, 0)
        # cur.clear()
        helper(0, cur, 1)

        return res
            
        # greedy approach
        # N = len(groups)
        # res1 = []
        # res2 = []

        # i, j = 0, 0

        # while i < N and groups[i] == 1:
        #     i += 1
        # if i < N:
        #     res1.append(words[i])

        # while j < N and groups[j] == 0:
        #     j += 1
        # if j < N:
        #     res2.append(words[j])

        # prev = 0
        # while i < N:
        #     if groups[i] != prev:
        #         res1.append(words[i])
        #         prev = prev ^ 1
        #     i += 1

        # prev = 1
        # while j < N:
        #     if groups[j] != prev:
        #         res2.append(words[j])
        #         prev = prev ^ 1
        #     j += 1
        
        # return res1 if len(res1) > len(res2) else res2
            
        


