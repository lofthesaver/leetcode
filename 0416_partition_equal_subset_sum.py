from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 1. Check if sum of nums is even, else cannot form two subsets
        if sum(nums) % 2 != 0:
            return False
        
        subset_sum = sum(nums) // 2
        
        # 2. Create an array to check whether a number between 1 and subset_sum can be formed
        # Loop through all numbers in nums and update the dp array,
        # Finally, check whether can_be_formed[subset_sum] == True
        can_be_formed = [True] + [False] * subset_sum

        for n in nums:

            # Update can_be_formed array for all values from subset_sum to 1
            for v in range(subset_sum, n - 1, -1):
                
                # Change can_be_formed[v] to True if can_be_formed[v - n] is True 
                # the dp array is updated backwards, from v = subset_sum to v = 1
                can_be_formed[v] = can_be_formed[v] or can_be_formed[v - n]

                # If v is subset_sum and it can be formed, return True
                if v == subset_sum and can_be_formed[v] == True:
                    return True
                
        return can_be_formed[subset_sum]
    

# print(Solution().canPartition(nums = [1, 5, 11, 5]))
# print(Solution().canPartition(nums = [1, 2, 3, 5]))
# print(Solution().canPartition(nums = [3, 3, 3, 4, 5]))