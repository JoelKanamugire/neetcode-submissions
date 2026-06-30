class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        NewS = set()
        for num in nums:
            if num in NewS:
                return True
            else:
                NewS.add(num)
        return False


        
     