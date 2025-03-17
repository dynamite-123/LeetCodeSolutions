class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = Counter(nums)
        for num in hm.values():
            if num & 1:
                return False
        return True
