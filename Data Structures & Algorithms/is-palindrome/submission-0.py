class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while R > L:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -=1
            elif s[L]. lower() != s[R].lower():
                return False
            else:
                R -=1
                L +=1
        return True

        