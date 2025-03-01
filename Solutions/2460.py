class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]: # type: ignore
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i], nums[i + 1] = nums[i] * 2, 0
            
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums