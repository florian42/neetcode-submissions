class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val and nums[right] != val:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                right = right - 1

            if nums[right] == val:
                right = right - 1
            if nums[left] != val:
                left = left + 1

        return len(nums[0:max(0, right + 1)])
