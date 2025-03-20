class Solution:
    def maxSum(self, nums: List[int]) -> int: # type: ignore
        sn = set()

        for num in nums:
            if num > 0:
                sn.add(num)
        return sum(list(sn)) if len(sn) else max(nums)

        # sn = set(nums)
        # res = flag = 0
        # for num in nums:
        #     if num >= 0:
        #         flag = 1
        #         break
        # if not flag:
        #     return max(nums)
        # for num in nums:
        #     if num in sn and num > 0:
        #         res += num
        #         sn.remove(num)
        # return res