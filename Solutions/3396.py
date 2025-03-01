class Solution:
    def minimumOperations(self, nums: List[int]) -> int: # type: ignore

        def check(nums) -> bool:
            return len(nums) == len(set(nums))
        
        res = 0
        while not check(nums):
            res += 1
            if len(nums) > 3:
                nums = nums[3:]
            else:
                nums = []
        
        return res