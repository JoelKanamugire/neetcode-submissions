class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashM = set()
        for n in nums:
            if n in hashM:
                return True
            else:
                hashM.add(n)
        return False