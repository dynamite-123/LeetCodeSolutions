from typing import List
from itertools import accumulate
import bisect

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        N = len(nums1)

        diff = sorted([abs(i - j) for i, j in zip(nums1, nums2)])

        # pref = [0] * (N + 1)
        # s = 0
        # for i, n in enumerate(diff):
        #     s += n
        #     pref[i + 1] = s

        # PREFIX SUM IN SINGLE LINE
        pref = [0] + list(accumulate(diff))
        
        sm = sum(diff)
        def ops(x):
            # MANUAL BINARY SEARCH OVER DIFF
            # l, r = 0, N
            # while l < r:
            #     mid = (l + r) // 2
            #     if diff[mid] > x:
            #         r = mid
            #     elif diff[mid] <= x:
            #         l = mid + 1

            # BINARY SEARCH USING INBUILT FUNCTION
            l = bisect.bisect_right(diff, x, lo=0, hi=N)
            
            sub = (N - l) * x
            return k - (sm - pref[l] - sub)

        l, r = 0, max(diff)

        while l < r:
            mid = (l + r) // 2

            if ops(mid) >= 0:
                r = mid
            else:
                l = mid + 1

        res = 0
        rem = ops(l)

        for x in diff:
            if x > l:
                x = l
            if x == l and rem > 0 and x > 0:
                rem -= 1
                x = x - 1
            res += x**2

        return res
            