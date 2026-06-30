class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for num in nums:
            if num not in Set:
                Set.add(num)
            else:
                return True
        return False
        