class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # Loop through array, apply operation
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Loop through array, if nums[i] != 0 then swap contents
        curr_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr_index], nums[i] = nums[i], nums[curr_index]
                curr_index += 1

        return nums