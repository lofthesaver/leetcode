from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        possible_nums = set(nums)
        res = []
        
        # Backtracking
        def backtrack(arr, curr_nums):

            # Base case: If the candidate is a solution, output it
            if len(arr) == n:
                res.append(arr)
                return

            # Iterate through all possible next candidates
            for next_num in possible_nums:

                # Check if the next candidate is valid
                if next_num not in curr_nums:

                    # Place the next candidate
                    arr = arr.copy()
                    arr.append(next_num)
                    curr_nums = curr_nums.copy()
                    curr_nums.add(next_num)

                    # Recursively call backtrack with the new candidate
                    backtrack(arr, curr_nums)

                    # Remove the candidate to backtrack and try other possibilities
                    arr = arr.copy()
                    arr.pop()
                    curr_nums = curr_nums.copy()
                    curr_nums.remove(next_num)

        # Call backtrack
        backtrack([], set())
        return res
    


print(Solution().permute(nums = [1,2,3]))
print(Solution().permute(nums = [0,1]))