class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        h = collections.defaultdict(list)

        for num in nums:
            s = 0
            n = num
            while n:
                s += n % 10
                n //= 10
            h[s].append(num)

        for nums in h.values():
            m = -1
            if len(nums) >= 2:
                nums.sort(reverse=True)
                m = sum(nums[0:2])
            res = max(m, res)

        return res