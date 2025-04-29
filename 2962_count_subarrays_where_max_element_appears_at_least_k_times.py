from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # Initial window
        left = 0

        # Record current maximum value and count
        max_value = max(nums)
        max_count = 0

        # Record result
        res = 0

        # Loop through right index
        for right in range(len(nums)):

            # Check if right element is the max value
            if nums[right] == max_value:
                max_count += 1

            # Determine whether the left side of the window needs to be contracted
            while left <= right and max_count >= k:

                # Remove left count if left element is current max
                if nums[left] == max_value:
                    max_count -= 1

                # Shrink the window
                left += 1

            # Once window is shrinked, left is the first index where condition is not satisfied
            res += left
        
        return res
        

print(Solution().countSubarrays(nums = [1,3,2,3,3], k = 2))
print(Solution().countSubarrays(nums = [1,4,2,1], k = 3))
print(Solution().countSubarrays([28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], k = 1))