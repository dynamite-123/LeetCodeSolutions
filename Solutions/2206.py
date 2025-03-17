class Solution:
    def divideArray(self, nums: List[int]) -> bool: # type: ignore
        hm = Counter(nums) # type: ignore
        for num in hm.values():
            if num & 1:
                return False
        return True
