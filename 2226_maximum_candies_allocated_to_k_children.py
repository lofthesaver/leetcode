class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        
        # Idea: set min_k = 0 and max_k = max(candies),
        # binary search for the maximum number

        # For each k, determine maximum candies by checking whether there are at least
        # k piles (for k children), where each pile has at least mid candies

        left = 1
        right = max(candies)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            # Calculate number of piles with at least mid candies, including splits
            tot = 0
            for pile in candies:
                tot += pile // mid

            # If can allocate, then move right
            if tot >= k:
                res = mid
                left = mid + 1
            
            else:
                right = mid - 1

        return res
    

print(Solution().maximumCandies(candies = [4,7,5], k = 4))