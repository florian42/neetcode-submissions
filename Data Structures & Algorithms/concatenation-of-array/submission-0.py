class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = [None] * len(nums) * 2
        picks = list(range(len(nums))) * 2

        for index, pick in enumerate(picks):
            new_array[index] = nums[pick]

        return new_array 
        