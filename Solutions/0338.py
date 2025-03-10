class Solution:
    def countBits(self, n: int) -> List[int]: # type: ignore
        # my approach
        # cache = {}
        # res = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     ones = 0
        #     t = i
        #     while t:
        #         if t in cache:
        #             ones += cache[t]
        #             break
        #         if t % 2:
        #             ones += 1
        #         t = t // 2
        #     res[i] = ones
        # return res
        res = [0] * (n + 1)
        sub = 1
        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            res[i] = res[i - sub] + 1
        return res