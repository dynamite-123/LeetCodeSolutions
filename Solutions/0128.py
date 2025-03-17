class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # type: ignore
        nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                max_count = max(max_count, length)
        return max_count

        # if not nums:
        #     return 0
        # nums = list(set(nums))
        # nums.sort()
        # max_count = 1
        # count = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1] + 1:
        #         count += 1
        #     else:
        #         count = 1
        #     max_count = max(count, max_count)

        # return max_count

