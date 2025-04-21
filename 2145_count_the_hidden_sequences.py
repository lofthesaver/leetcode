from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        # Idea: prefix sum the differences array, find the minimum and maximum 
        # Then the number of possible sequences = (upper - lower) - (maximum - minimum),
        # 0 if there is no possible sequence

        prefix_sum = [0] * (len(differences) + 1)
        prefix_sum[0] = 0

        for i in range(len(differences)):
            prefix_sum[i + 1] = prefix_sum[i] + differences[i]

        return max(0, (upper - lower + 1) - (max(prefix_sum) - min(prefix_sum)))


print(Solution().numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6))
print(Solution().numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5))
print(Solution().numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6))
print(Solution().numberOfArrays(differences = [-40], lower = -46, upper = 53))
