from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # Idea: iterate through range(0, len(nums) - 2), 
        # if current number is 0 flip the next 3,
        # at the end check whether the last 3 elements are flipped
        count = 0
        for i in range(0, len(nums) - 2):
            print(nums)
            if nums[i] == 0:
                count += 1
                nums[i], nums[i + 1], nums[i + 2] = 1, int(not nums[i + 1]), int(not nums[i + 2])

        return count if nums[i] == nums[i + 1] == nums[i + 2] == 1 else -1
        

print(Solution().minOperations(nums = [0,1,1,1,0,0]))