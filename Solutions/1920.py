from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [None] * N

        for i in nums:
            ans[i] = nums[nums[i]]

        return ans