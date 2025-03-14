class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # type: ignore
        hm = defaultdict(int) # type: ignore
        heap = []
        res = []
        for num in nums:
            hm[num] += 1
        for num, freq in hm.items():
            heapq.heappush(heap, [-freq, num]) # type: ignore
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # type: ignore
        return res