class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        totalC = 0
        r = len(s) - 1

        while s[r] == ' ':
            r -= 1

        while r >= 0 and s[r] != ' ':
            r -=1
            totalC +=1

        return totalC

        