class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if num not in temp:
                temp.append(num)
        nums[:] = temp
        