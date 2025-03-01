class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int: # type: ignore
        res = 0
        n, m = len(nums1), len(nums2)
        if n % 2:
            for num in nums2:
                res ^= num
        if m % 2:
            for num in nums1:
                res ^= num
        return res