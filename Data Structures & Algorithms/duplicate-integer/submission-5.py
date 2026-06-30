class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashM = set()
        for num in nums:
            if num in hashM:
                return True
            else:
                hashM.add(num)
        return False