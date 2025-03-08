class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i = j = 0   
        visited = [[0, 0]]
        temp = 'NWSE'
        d = temp[0]
        for s in instructions:
            if s == 'G':
                if d == 'N':
                    j += 1
                elif d == 'S':
                    j -= 1
                elif d == 'E':
                    i -= 1
                elif d == 'W':
                    i += 1
                t = [i, j]
                visited.append(t)
            elif s == 'L':
                k = temp.index(d)
                d = temp[(k + 1) % 4]
            elif s == 'R':
                k = temp.index(d)
                d = temp[(k - 1) % 4]
        return False if d == 'N' and [i, j] != [0, 0] else True