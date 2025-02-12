class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = x
        rev = 0
        while(t > 0):
            rev = rev * 10 + t % 10
            t = t//10
        if rev == x:
            return True