class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: # type: ignore
        res = []

        intervals.sort()
        l, r = intervals[0]
        for i, j in intervals:
            if r >= i:
                r = max(j, r)
            else:
                res.append([l, r])
                l, r = i, j
        res.append([l, r])

        return res