class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashM = {}
        for num in nums:
            if num not in HashM:
                HashM[num] = 1
            else:
                return True
        return False



     