class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int: # type: ignore
        min_sum, max_sum = float("inf"), float("-inf")
        s1 = s2 = 0

        for num in nums:
            s1 += num
            s2 += num
            if s1 < num: s1 = num
            if s2 > num: s2 = num
            max_sum = max(max_sum, s1)
            min_sum = min(min_sum, s2)

        return max(abs(min_sum), abs(max_sum))