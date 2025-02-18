class Solution:
    def singleNumber(self, nums: List[int]) -> int: # type: ignore
        res = 0

        for num in nums:
            res = num ^ res

        return res