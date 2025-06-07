import heapq
from collections import defaultdict
class Solution:
    def clearStars(self, s: str) -> str:
        N = len(s)
        heap = [] # To find the smallest character
        hm = defaultdict(list) # To find the rightmost idx of the smallest character
        keep = [True] * N

        for i in range(N):
            if s[i] == '*':
                smallest = heapq.heappop(heap)
                idx = hm[smallest].pop()
                keep[i] = False
                keep[idx] = False
            else:
                heapq.heappush(heap, s[i])
                hm[s[i]].append(i)

        return ''.join(s[i] for i in range(N) if keep[i])
