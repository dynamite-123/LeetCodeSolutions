class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'        
        res = 0
        for char in s[0: k]:
            if char in vowels:
                res += 1
        maxi = res
        for i in range(k, len(s)):
            if s[i] in vowels:
                res += 1
            if s[i-k] in vowels:
                res -= 1
            maxi = max(maxi, res)
        
        return maxi
