class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return [-1, -1]
        
        # for i, n in enumerate(nums):
        #     l, r = i, len(nums) - 1
        #     while(r > l):
        #         twoSum = nums[l] + nums[r]
        #         if(twoSum > target):
        #             r -= 1
        #         elif(twoSum < target):
        #             l += 1
        #         else:
        #             return [l+1, r+1]