class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int: #type: ignore
        high = diff = res = 0

        for num in nums:
            res = max(res, diff * num)
            diff = max(high - num, diff)
            high = max(high, num)
        return res

        # N = len(nums)
        # pro = [0] * N

        # temp = nums[-1]
        # for i in range(N - 1, -1, -1):
        #     temp = max(temp, nums[i])
        #     pro[i] = temp
        
        # res = 0
        # for i in range(N - 2):
        #     for j in range(i+1, N - 1):
        #         res = max(res, (nums[i] - nums[j]) * pro[j + 1])
        # return res