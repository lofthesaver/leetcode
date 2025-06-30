from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        
        # Set left as min and right as max of subsequence
        left = 0

        # Record result
        res = 0

        for right in range(len(nums)):
            
            # If difference less than 1, increment right
            while nums[right] - nums[left] > 1:
                left += 1

            # If difference equal 1, record length of subsequence
            if nums[right] - nums[left] == 1:
                res = max(right - left + 1, res)

        return res


print(Solution().findLHS(nums = [1,3,2,2,5,2,3,7]))
print(Solution().findLHS(nums = [1,2,3,4]))
print(Solution().findLHS(nums = [1,1,1,1]))