class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: # type: ignore
        res = set(nums)

        for num in nums:
            if num not in res:
                res.add(num)
            else:
                res.remove(num)

        return list(res)