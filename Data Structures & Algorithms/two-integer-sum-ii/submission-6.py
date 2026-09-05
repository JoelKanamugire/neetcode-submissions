class Solution:
    def twoSum(self, numbers: List[int], target: [int]) -> List[int]:
        HashM = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in HashM:
                return [HashM[diff] + 1, i + 1]
            else:
                HashM[n] = i