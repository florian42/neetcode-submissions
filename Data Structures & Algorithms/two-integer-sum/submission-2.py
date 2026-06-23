class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            print(seen)
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

        raise ValueError("Invariant: every input has exactly one pair of indices i and j that satisfy the condition.")