from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # Idea: use bactracking to find all subsets, and for each subset
        # return the XOR total, then finally sum all subsets
        subset_sums = []

        # Backtracking
        def backtrack(lst, starting_index):

            # Calculate XOR of this subset
            xor = 0
            for v in lst:
                xor ^= v
            subset_sums.append(xor)

            # Loop through all possible candidates to add to list
            for i in range(starting_index, len(nums)):

                # Add element to lst
                lst.append(nums[i])

                # Call backtrack
                backtrack(lst, i + 1)

                # Remove the last added element
                lst.pop()

        # Call backtrack and return result
        backtrack([], 0)
        return sum(subset_sums)


print(Solution().subsetXORSum(nums = [1,3]))
print(Solution().subsetXORSum(nums = [5,1,6]))
print(Solution().subsetXORSum(nums = [3,4,5,6,7,8]))