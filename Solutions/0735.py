class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]: # type: ignore
        ass = [asteroids[0]]

        for num in asteroids[1:]:
            ass.append(num)
            while(1):
                if len(ass) >= 2 and (ass[-1] < 0 and ass[-2] > 0):
                    t1, t2 = ass.pop(), ass.pop()
                    if abs(t1) > abs(t2):
                        ass.append(t1)
                    elif abs(t2) > abs(t1):
                        ass.append(t2)
                else: 
                    break
        return ass
