class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            print("=======")
            for j, num_j in enumerate(nums[1:]):
                normalied_j = j + 1
                sum = num_i + num_j
                print(f"")
                print(f"[{i}, {num_i}] --> [{normalied_j}, {num_j}] = {sum}")
                if sum == target and i != normalied_j:
                    return [i, normalied_j]
            print("=======")
        raise ValueError("Invariant: every input has exactly one pair of indices i and j that satisfy the condition.")