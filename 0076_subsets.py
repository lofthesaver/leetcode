from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> int:

        # Idea: use bactracking to find all subsets
        all_subsets = []

        # Backtracking
        def backtrack(lst, starting_index):

            # Add lst to result
            all_subsets.append(lst[:])

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
        return all_subsets


print(Solution().subsets(nums = [1,2,3]))
print(Solution().subsets(nums = [5,1,6]))
print(Solution().subsets(nums = [3,4,5,6,7,8]))