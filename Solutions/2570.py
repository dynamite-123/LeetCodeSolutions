class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]: # type: ignore
        hm = defaultdict(int) # type: ignore
        for num in nums1:
            hm[num[0]] += num[1]

        for num in nums2:
            hm[num[0]] += num[1]

        res = list(hm.items())
        res.sort()
        return res