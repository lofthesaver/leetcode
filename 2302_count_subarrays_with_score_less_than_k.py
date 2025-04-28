from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # Sliding window, loop thorugh right indices,
        # for each right index move left index until solution is valid

        # Initiate current sum
        curr_sum = 0

        # Initiate left index
        left = 0

        # Initiate result
        res = 0

        for right in range(len(nums)):
            
            # Add right value
            curr_sum += nums[right]

            # Move left index until solution is valid
            while left <= right and curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            
            res += (right - left + 1)

        return res
    

print(Solution().countSubarrays(nums = [2,1,4,3,5], k = 10))
# print(Solution().countSubarrays(nums = [1,1,1], k = 5))