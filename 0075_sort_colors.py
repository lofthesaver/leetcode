from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Bubble Sort
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):

                # Check if need to swap
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
    
print(Solution().sortColors(nums = [2,0,2,1,1,0]))
print(Solution().sortColors(nums = [2,0,1]))
