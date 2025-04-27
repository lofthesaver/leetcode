from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n - 2):
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                res += 1

        return res
    
print(Solution().countSubarrays(nums = [1,2,1,4,1]))
print(Solution().countSubarrays(nums = [1,1,1]))