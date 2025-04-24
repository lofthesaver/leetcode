from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        # Loop through each left index, find the minimum right index that makes the array complete
        # For each subsequent left index, remove the previous left index

        # Count distinct elements
        distinct_elems = len(set(nums))

        # Keep track of current elements and number of distinct elements
        curr_elems = {}

        # Set right index
        right = 0

        # Set count of complete arrays
        complete_arrays = 0

        # Loop through left index
        for left in range(len(nums)):

            # Remove value at previous left index
            if left != 0:
                prev_elem = nums[left - 1]
                curr_elems[prev_elem] -= 1
                if curr_elems[prev_elem] == 0:
                    curr_elems.pop(prev_elem)

            # Increment right index until number of distinct elements == distinct_elems
            while len(curr_elems) != distinct_elems and right < len(nums):

                # Add right element
                right_elem = nums[right]
                curr_elems[right_elem] = curr_elems.get(right_elem, 0) + 1

                # Increment right index
                right += 1

            # If after while loop still not complete then break
            if len(curr_elems) != distinct_elems:
                break

            # Add the number of complete arrays for this left index to total
            complete_arrays += (len(nums) - right + 1)

        # Return count of complete arrays
        return complete_arrays


# print(Solution().countCompleteSubarrays(nums = [1,3,1,2,2]))
# print(Solution().countCompleteSubarrays(nums = [5,5,5,5]))