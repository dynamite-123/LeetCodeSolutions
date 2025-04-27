from typing import List
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(2, len(nums)):
            if nums[i] + nums[i-2] == nums[i-1] / 2:
                res += 1
        return res