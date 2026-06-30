class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_hash = {}
        for i, n in enumerate (nums):
            diff = target - n
            if diff in new_hash:
                return [new_hash[diff], i]
            else:
                new_hash[n] = i 
        return new_hash
      
        
   