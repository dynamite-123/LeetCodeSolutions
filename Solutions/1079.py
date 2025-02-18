class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        freq = collections.Counter(tiles) # type: ignore
        def backtrack():
            res = 0
            # - auto base case when the counts of all chars is zero in freq
            for c in freq:
                if freq[c]:
                    freq[c] -= 1
                    res += 1
                    res += backtrack()
                    freq[c] += 1
            return res
        return backtrack()