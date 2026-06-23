class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        safe_index = 0
        seen = None

        for index in range(len(nums)):
            if index == len(nums) - 1:
                return len(nums[0:safe_index+1])
            current_num = nums[index]
            next_num = nums[index + 1]

            if current_num == next_num:
                seen = current_num
                continue

            if current_num != next_num:
                nums[safe_index + 1] = next_num
                safe_index = safe_index + 1
                seen = current_num

            
        raise Exception("Should always return as part of the loop")
