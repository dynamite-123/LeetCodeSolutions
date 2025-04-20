class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        N = len(nums)
        res = 0
        nums.sort()

        for ind, num in enumerate(nums[:-1]):
            li, ri = N, -1
            l, r = ind + 1, N - 1
            while l <= r:
                mid = (l + r) // 2
                if num + nums[mid] <= upper:
                    l = mid + 1
                    ri = mid
                else: 
                    r = mid - 1

            l, r = ind + 1, N - 1
            while l <= r:
                mid = (l + r) // 2
                if num + nums[mid] >= lower:
                    r = mid - 1
                    li = mid
                else:
                    l = mid + 1
            if li <= ri:
                res += ri - li + 1
        return res
            