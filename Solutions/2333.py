from typing import List
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # binary search solution 
        # time complexity: O(N * logT) (T = range of delta)
        # space complexity: O(N)
        N, k = len(nums1), k1 + k2

        delta = [abs(i-j) for i, j in zip(nums1, nums2)]
        delta.sort()

        def calc(target):
            ops = 0
            for n in delta:
                if n > target:
                    ops += n - target
            return ops
        def good(target):
            return calc(target) <= k

        l, r = 0, max(delta)

        while l < r:
            mid = (l + r) // 2

            if good(mid):
                r = mid

            else:
                l = mid + 1
        
        krem = k - calc(r)

        res = 0
        for x in delta:
            if x > r:
                x = r
            if x == r and krem > 0 and x > 0:
                x -= 1
                krem -= 1
            res += x**2
        return res