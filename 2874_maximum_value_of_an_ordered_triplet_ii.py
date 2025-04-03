from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # Idea: use prefix and suffix sum to store greatest value before/after current index (exclusive)
        # Then, loop through j values and find maximum triplet value
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i - 1], nums[i - 1])
        
        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = max(suffix[i + 1], nums[i + 1])

        # Loop through j values and find maximum of prefix[j] - nums[j] * suffix[j]
        res = 0
        for j in range(len(nums)):
            res = max(res, (prefix[j] - nums[j]) * suffix[j])

        return res



print(Solution().maximumTripletValue(nums = [12,6,1,2,7]))
print(Solution().maximumTripletValue(nums = [1,10,3,4,19]))