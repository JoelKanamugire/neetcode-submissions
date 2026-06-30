class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range(2):
            for num in nums:
                new_array.append(num)
        return new_array

        