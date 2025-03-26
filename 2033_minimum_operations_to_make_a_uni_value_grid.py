from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        # Idea: take median (by sorting), count the number of operations
        # it takes to get all numbers to the median

        lst = [v for row in grid for v in row] 
        lst.sort()

        # Get median
        median = lst[len(lst)//2]

        # Loop through all elements and add total operations
        total_operations = 0
        for v in lst:

            # If not possible to get the median from v using x
            if abs(median - v) % x != 0:
                return -1

            # Add operation count
            total_operations += (abs(median - v) / x)

        return int(total_operations)


print(Solution().minOperations(grid = [[2,4],[6,8]], x = 2))
print(Solution().minOperations(grid = [[1,5],[2,3]], x = 1))
print(Solution().minOperations(grid = [[1,2],[3,4]], x = 2))