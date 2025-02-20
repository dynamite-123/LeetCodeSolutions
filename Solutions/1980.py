class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str: # type: ignore
        n = len(nums)
        nums = [int(x, 2) for x in nums]

        res = -1
        result = ['0'] * n
        for i in range(2**  n):
            if i not in nums:
                res = i
                break

        for i in range(n-1, -1, -1):
            if not res:
                break
            print(i)
            result[i] = str(res % 2)
            res = res // 2
 
        return "".join(result)

    # - tryhard
        # return ''.join(str(1 - int(nums[i][i])) for i in range(len(nums))) 

