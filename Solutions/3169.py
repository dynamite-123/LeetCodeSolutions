class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int: #type: ignore
        meetings.sort()
        l, r = meetings[0]
        for i, j in meetings:
            if r >= i:
                r = max(r, j)
            else:
                days -= r - l + 1
                l, r = i, j
        return days - (r - l + 1)

        # - Brute force
        # sd = set()
        # for i in range(1, days + 1): sd.add(i)

        # for l, r in meetings:
        #     for i in range(l, r + 1):
        #         if i in sd:
        #             sd.remove(i)
        # return len(sd)