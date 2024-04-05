class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #sum of all numbers upto len(nums) - sum of numbers in the array nums will give you the required answer
        return int(len(nums)*(len(nums)+1)/2 - sum(nums))

#my first solution which is inefficient
'''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i'''
