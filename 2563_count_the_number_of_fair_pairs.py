from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # 1. Sort the array
        nums.sort()

        # 2. For each number, find the left and right bounds of all numbers that satisfy the condition,
        # for each subsequent number decrease the bounds until condition is satisfied

        # Set initial left and right bound
        left = len(nums) - 1
        right = len(nums) - 1

        # Result - stores number of total fair pairs
        fair_pairs = 0

        # Loop through each number
        for i, v in enumerate(nums):

            left = max(left, i)
            right = max(right, i)

            # Find left bound that satisfies condition
            # left = index of first value that does not satisfy the condition
            while v + nums[left] >= lower and left > i:
                left -= 1

            # Find right bound that satisfies condition
            # right = index of last value that satisfies condition
            while v + nums[right] > upper and right > i:
                right -= 1

            # If either left or right out of bounds, or if left is left of the current index, then return
            if left < 0 or right < 0:
                return fair_pairs
            
            # Add the number of values between left and right to fair_pairs
            fair_pairs += (right - left)
            
        return fair_pairs


# print(Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
# print(Solution().countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))
# print(Solution().countFairPairs(nums = [0,0,0,0,0,0], lower = 0, upper = 0))