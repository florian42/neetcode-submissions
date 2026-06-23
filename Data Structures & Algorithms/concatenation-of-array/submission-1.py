class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = [None] * len(nums) * 2

        for index in range(2*len(nums)):
            new_array[index] = nums[index % len(nums)]

        return new_array 
        