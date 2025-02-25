class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int: # type: ignore
        curSum = odd = 0
        even = 0
        res = 0

        for num in arr:
            curSum += num
            if curSum % 2: 
                odd += 1
                res += even + 1
            else:
                even += 1
                res += odd

        return res % (10**9 + 7) 

        # curSum = odd = 0
        # even = 1

        # for num in arr:
        #     curSum += num
        #     if curSum % 2: odd += 1 
        #     else: even += 1

        # return odd * even % (10**9 + 7) 
        


        