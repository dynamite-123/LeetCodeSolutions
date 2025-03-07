class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # type: ignore
        visited = {}
        for s in strs:
            t = list(s)
            t.sort()
            t = "".join(t)
            if t not in visited:
                visited[t] = [s]
            else:
                visited[t].append(s)

        return [i for i in visited.values()]