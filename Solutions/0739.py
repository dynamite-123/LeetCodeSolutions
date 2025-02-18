class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # type: ignore
        stack = [] # - ind
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append(i)
        return res

        '''
        stack = [] # - temp, ind
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res
        '''