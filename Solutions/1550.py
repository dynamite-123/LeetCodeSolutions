from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3:
            return False

        count = arr[0] % 2 + arr[1] % 2 + arr[2] % 2
        
        for r in range(3, N):
            if count == 3:
                return True
            count = count - arr[r - 3] % 2 + arr[r] % 2
        if count == 3:
            return True

        return False