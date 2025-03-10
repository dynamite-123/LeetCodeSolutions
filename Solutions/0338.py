class Solution:
    def countBits(self, n: int) -> List[int]: # type: ignore
        # my approach
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            ones = 0
            if i % 2:
                ones += 1
            ones += res[i // 2]
            res[i] = ones
        return res

        ##another way
        # res = [0] * (n + 1)
        # sub = 1
        # for i in range(1, n + 1):
        #     if sub * 2 == i:
        #         sub = i
        #     res[i] = res[i - sub] + 1
        # return res