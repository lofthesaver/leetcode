class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        
        
        # Idea: run Kadane's algortihm twice, one for maxSum, one for minSum
        # Kadane's algorithm will find max (or min) sum of subarray in O(n) time

        # max sum
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_value = nums[i]

            # If curr_sum is negative, start a new subarray with curr_value,
            # else continue to add to curr_sum
            if curr_sum < 0:
                curr_sum = curr_value

            else:
                curr_sum += curr_value

            # Record max sum
            max_sum = max(max_sum, curr_sum)


        # Repeat for min sum
        min_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_value = nums[i]

            # If curr_sum is positive, start a new subarray with curr_value,
            # else continue to add to curr_sum
            if curr_sum > 0:
                curr_sum = curr_value

            else:
                curr_sum += curr_value

            # Record max sum
            min_sum = min(min_sum, curr_sum)


        # return maximum of max_sum, abs(min_sum), and 0
        return max((max_sum, abs(min_sum), 0))