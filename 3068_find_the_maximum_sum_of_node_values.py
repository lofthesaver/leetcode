from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        # 1. Go through each node, and store the difference between itself
        # and itself XOR k
        differences = [(v ^ k) - v for v in nums]

        # 2. Sort the differences
        differences.sort(reverse = True)

        # 3. Go through all positive differences and add to the result (pair by pair)
        res = sum(nums)
        for i in range(0, len(nums), 2):

            # If no more pairs
            if i + 1 == len(nums):
                break

            # If possible to add to result
            if differences[i] + differences[i + 1] > 0:
                res += differences[i] + differences[i + 1]

        return res

        
print(Solution().maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]))
print(Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]))
print(Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))
