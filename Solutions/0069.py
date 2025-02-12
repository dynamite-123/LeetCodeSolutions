class Solution(object):
    def mySqrt(self, x):
        beg = 0
        end = x
        while(beg <= end):
            mid = (beg + end)//2
            num = mid
            if x == 1:
                return 1
            elif (num*num == x) or ((num+1)*(num+1) > x and (num*num) < x):
                return num
            elif num*num < x:
                beg = num + 1
            else:
                end = num - 1
        return 0