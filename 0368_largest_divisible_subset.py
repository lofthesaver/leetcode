from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        # Idea: 
        # 1. Sort the list
        # 2. O(n^2) loop through the entire list, and compare pairs
        # 3. For each pair, if condition satisfied, then update the dp list
        # to store the longest current subset ending in this current number

        nums.sort()

        # Initialize list to store the longest subset ending in the particular number
        subsets = [[n] for n in nums]

        # Loop through the entire list
        for i in range(len(nums)):
            for j in range(i):

                # Check condition
                if nums[i] % nums[j] == 0:

                    # If condition satisfied, add nums[i] to the subset 
                    # if the length of the subset with j is greater than 
                    # the length of the subset with i
                    if len(subsets[j]) + 1 > len(subsets[i]):
                        subsets[i] = subsets[j] + [nums[i]]

        # Find subset with maximum length
        max_length = 0
        max_subset = []
        for subset in subsets:
            if len(subset) > max_length:
                max_length = len(subset)
                max_subset = subset

        return max_subset
    
    
print(Solution().largestDivisibleSubset(nums = [1,2,3]))
print(Solution().largestDivisibleSubset(nums = [1,2,4,8]))