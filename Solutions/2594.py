class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int: # type: ignore
        #initially didn't hashmap
        #hashmap increases efficiency as duplicate ranks may exist
        ranks = Counter(ranks)  # type: ignore
        def max_cars(mins: int) -> int:
            res = 0
            for rank, v in ranks.items():
                res += v * math.floor(math.sqrt(mins // rank)) # type: ignore
            return res
        
        l, r = 0, max(ranks) * int(math.pow(cars, 2)) # type: ignore
        res = 0
        while l <= r:
            mid = (l + r) // 2
            k = max_cars(mid)
            if k < cars:
                l = mid + 1
            elif k >= cars:
                res = mid
                r = mid - 1
        return res