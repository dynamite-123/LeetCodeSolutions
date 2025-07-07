from collections import defaultdict
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.hm1 = defaultdict(int)
        self.hm2 = defaultdict(int)
        
        for n in nums1: self.hm1[n] += 1
        for n in nums2: self.hm2[n] += 1

        self.sortedkeys = sorted(self.hm1.keys())

    def add(self, index: int, val: int) -> None:
        self.hm2[self.nums2[index]] -= 1
        self.hm2[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for key in self.sortedkeys:
            if key >= tot: break
            res += self.hm1[key] * self.hm2[tot - key]

        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)