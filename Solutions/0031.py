class Solution:
    def nextPermutation(self, nums: List[int]) -> None: # type: ignore
        """
        Do not return anything, modify nums in-place instead.
        """
            
        n = len(nums)

        if n < 2: 
            return

        bp = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]: 
                bp = i - 1
                break

        if bp == -1: 
            nums.sort()
            return

        for i in range(n-1, bp, -1):
            nums[i]
            if nums[bp] < nums[i]:
                nums[bp], nums[i] = nums[i], nums[bp]
                break

        nums[:] = nums[0:bp+1] + sorted(nums[bp+1:n])