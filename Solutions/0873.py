class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int: # type: ignore
        res = 0
        elements = set(arr)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                curr, prev = arr[j], arr[i]
                nex = curr + prev

                length = 2
                while nex in elements:
                    prev, curr = curr, nex
                    nex = curr + prev
                    length += 1
                
                res = max(res, length)

        return res if res > 2 else 0