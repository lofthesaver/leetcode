from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        # Idea: use binary search to find the smallest difference that can be satisfied

        # Function which takes in the difference and checks whether there are at least p pairs
        # which satisfies the minimum difference
        def condition(min_diff) -> bool:

            # Count number of pairs that satisfy the min difference
            num_of_pairs = 0

            # Loop through nums and check each pair
            i = 0
            while i < len(nums) - 1:
             
                # Check if this pair satisfies the condition
                if abs(nums[i] - nums[i + 1]) <= min_diff:

                    # If satisfy condition, add 1 to number of pairs and skip the next index (since next i is already used)
                    num_of_pairs += 1
                    i += 1
                
                i += 1

            # If number of pairs that satisfy the min diff >= p, then the difference is satisfiable,
            # else not satisfiable
            return num_of_pairs >= p


        # Sort nums
        nums.sort()

        # Set minimum and maximum difference
        left, right = 0, nums[-1] - nums[0]

        # Binary search
        while left < right:

            # This mid formula works if finding the minimum left value which satisfies the condition;
            # to find maximum, use mid = left + (right - left + 1) // 2
            mid = left + (right - left) // 2

            # If the difference can be satisfied, then move right, else move left
            if condition(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
    
print(Solution().minimizeMax(nums = [10,1,2,7,1,3], p = 2))
print(Solution().minimizeMax(nums = [4,2,1,2], p = 1))
print(Solution().minimizeMax(nums = [3,4,2,3,2,1,2], p =3))