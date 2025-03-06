class Solution:
    def findMissingAndRepeatedValues(self, grid):
        
        # Idea:
        # Find the sum of all numbers, so that sum = real_sum + a - b
        # Then, find the sum of all numbers squared, so that squared_sum = real_squared_sum + a^2 - b^2

        # Use the two equations to solve for a and b

        # size of grid
        n = len(grid)

        # Calculate sums
        s = 0
        ss = 0
        for i in range(n):
            for j in range(n):
                s += grid[i][j]
                ss += grid[i][j] ** 2

        # Set i = n**2 (so number range from 1 to i)
        i = n ** 2

        # Find real sums - sum of arithmetic series
        rs = int(i * (i + 1) / 2)

        # Find real squared sum - sum of squares of first i natural numbers 
        rss = int((i * (i + 1) * (2 * i + 1)) / 6)

        # Find a and b using the two sums
        # 2a = [(ss - rss)/(s - rs)] + (s - rs)
        a = int((((ss - rss) / (s - rs)) + (s - rs))/2)
        b = int(rs + a - s)

        return [a, b]

print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))