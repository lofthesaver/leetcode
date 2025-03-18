from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        # Idea: Sliding window, use a OR mask to keep track of all the bits seen before the current number,
        # if mask & curr_elem != 0, it means that the current element shares a bit with some element
        # in the window, then move window to the right
    
        left, right = 0, 0

        # Keeps track of curent or
        curr_or = 0

        # Keep track of longest subarray
        longest_subarray = 0

        while right < len(nums):

            # Determine whether the left side of the window needs to be contracted
            while left < right and (curr_or & nums[right]) != 0:

                # Remove left element from window
                curr_or = curr_or ^ nums[left]

                # Shrink the window
                left += 1

            # Keep track of current longest subarray
            longest_subarray = max(longest_subarray, right - left + 1)
                
            # v is the character that will be added to the window
            v = nums[right]
            curr_or = curr_or | v

            # Expand the window
            right += 1

        return longest_subarray
    
print(Solution().longestNiceSubarray(nums = [1,3,8,48,10]))
print(Solution().longestNiceSubarray(nums = [3,1,5,11,13]))