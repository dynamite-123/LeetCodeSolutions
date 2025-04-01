class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]: #type: ignore
        S, P = len(spells), len(potions)
        res = [0] * S

        potions.sort()

        def number_of_potions(ind: int) -> int:
            l, r = 0, P - 1
            prev = P
            while l <= r:
                m = l + (r - l) // 2
                p = potions[m] * spells[ind]

                if p < success:
                    l = m + 1
                elif p >= success:
                    prev = m
                    r = m - 1
            return P - prev
        
        for i in range(S):
            res[i] = number_of_potions(i)
        return res