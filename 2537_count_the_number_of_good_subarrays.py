from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        # 1. Loop through each number as index left
        # 2. For index left, iterate right until array is not good
        # Once the array is not good, add to total and go to next left value

        # Count of occurences of each value
        occurences_count = {}

        # Set right index
        right = -1

        # Record total count of good subarrays
        good_subarrays = 0

        # Count pairs of matching indices
        pairs = 0

        # Loop through left indices
        for left in range(len(nums)):
            # print(occurences_count)

            # Iterate right until array is not good
            while pairs < k and right + 1 < len(nums):

                right += 1
                # Add current right value to dictionary
                occurences_count[nums[right]] = occurences_count.get(nums[right], 0) + 1

                pairs += (occurences_count[nums[right]] - 1) # since each new index will create n - 1 new pairs


            # If array is good, add to good subarrays
            if pairs >= k:

                # Array is now good, add this array and all remaining arrays to total count
                good_subarrays += (len(nums) - right)

            # Remove current left from the count dictionary
            occurences_count[nums[left]] -= 1

            # Update the number of pairs based on removed value
            pairs -= (occurences_count[nums[left]])

        return good_subarrays

        
print(Solution().countGood(nums = [1,1,1,1,1], k = 10))
print(Solution().countGood(nums = [3,1,4,3,2,2,4], k = 2))
