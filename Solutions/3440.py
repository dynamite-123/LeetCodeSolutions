from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        gaps = []

        prev = 0
        for i in range(n):
            gaps.append(startTime[i] - prev)
            prev = endTime[i]
        gaps.append(eventTime - endTime[-1])

        temp = 0
        res = 0
        for i in range(1, n):
            temp = max(temp, gaps[i-1])
            if temp >= endTime[i] - startTime[i]:
                res = max(res, endTime[i] - startTime[i] + gaps[i] + gaps[i+1])
            else:
                res = max(res, gaps[i] + gaps[i+1])

        temp = 0
        for i in range(n-2, -1, -1):
            temp = max(temp, gaps[i+2])
            if temp >= endTime[i] - startTime[i]:
                res = max(res, endTime[i] - startTime[i] + gaps[i] + gaps[i+1])
            else:
                res = max(res, gaps[i] + gaps[i+1])

        return res