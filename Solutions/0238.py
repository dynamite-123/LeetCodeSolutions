class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # type: ignore

        n = len(nums)
        tmul = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                tmul = tmul * num
        if zeroes > 1:
            return [0 for i in range(n)]
        elif zeroes == 1:
            return [0 if nums[i] != 0 else tmul for i in range(n)]
        else:
            return [tmul // nums[i] for i in range(n)]

        '''
        
        #prefix product method
        n = len(nums)
        result = [1] * n

        # First pass: Calculate prefix products
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
            print(result)

        # Second pass: Calculate suffix products on the fly
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            print(result, suffix)

        return result
        '''
        
        