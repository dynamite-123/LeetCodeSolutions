class Solution:
    def minimumIndex(self, nums: List[int]) -> int: # type: ignore
        N = len(nums)
        hm = Counter(nums) # type: ignore
        max_ele = max(hm, key=hm.get)
        pre, post = 0, nums.count(max_ele)

        if post < N // 2 + 1: return -1


        for i, num in enumerate(nums):
            if num == max_ele:
                pre += 1
                post -= 1
            if pre >= (i + 1) // 2 + 1 and post >= (N - (i + 1)) // 2 + 1:
                return i
        return -1

        # N = len(nums)
        # hm = defaultdict(int)
        # max_ele = 0
        # post = 0

        # for num in nums: hm[num] += 1
        # for num in hm:
        #     if hm[num] > N // 2:
        #         max_ele = num
        #         post = hm[num]
        # if max_ele == 0: return -1
        
        # pre = 0

        # for i, num in enumerate(nums):
        #     if num == max_ele:
        #         pre += 1
        #         post -= 1
        #     if pre >= (i + 1) // 2 + 1 and post >= (N - (i + 1)) // 2 + 1:
        #         return i
        # return -1
            
