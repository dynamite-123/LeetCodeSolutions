class Solution:
    def rob(self, nums: List[int]) -> int: # type: ignore
        N = len(nums)

        if N == 1:
            return nums[0]

        def helper(numbers):
            n = len(numbers)
            rob1 = rob2 = 0
            for num in numbers:
                curr = max(rob2, rob1 + num)
                rob1 = rob2
                rob2 = curr
                print(rob1, rob2)
            return rob2
        return max(helper(nums[0 : N - 1]), helper(nums[1:]))