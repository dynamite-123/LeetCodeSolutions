class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
        res = []
        count = collections.Counter(nums1) # type: ignore

        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res



        # res = []

        # for num in nums2:
        #     if num in nums1:
        #         res.append(num)
        #         nums1.remove(num)

        # return res