class Solution:
    def findPeakElement(self, nums: List[int]) -> int: #type: ignore
        # return nums.index(max(nums))
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid

        