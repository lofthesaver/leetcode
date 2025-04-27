from typing import List
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        # Set initial prefix sum
        prefix_sum = 0

        # Dictionary to record counts
        counts = Counter([0])

        # Record result
        res = 0

        # Loop through each index
        for i in range(len(nums)):

            # Calculate prefix sum, increment if nums[i] % mod == k
            if nums[i] % modulo == k:
                prefix_sum += 1

            # Record result
            res += counts[(prefix_sum - k + modulo) % modulo]

            # Increment count dictionary
            curr_count = prefix_sum % modulo
            counts[curr_count] = counts.get(curr_count, 0) + 1

        return res
        


print(Solution().countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1))
print(Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0))