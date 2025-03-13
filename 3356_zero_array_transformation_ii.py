from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        # Idea: binary search for the minimum value k such that the sequence can be processed

        # Function to check whether the given set of queries forms a zero array
        def zero_array(nums, queries):

            # Use a difference array & prefix sum to process queries in O(1),
            # then prefix sum witih O(n)
            prefix_sum = [0] * (len(nums) + 1)

            # Process queries
            for query in queries:
                start, end, amount = query[0], query[1], query[2]
                prefix_sum[start] += amount
                if end + 1 < len(nums):
                    prefix_sum[end + 1] -= amount

            for i in range(1, len(prefix_sum)):
                prefix_sum[i] += prefix_sum[i - 1]

            # Loop through nums, check if all values are negative after applying prefix sum
            for i in range(len(nums)):
                if nums[i] - prefix_sum[i] > 0:
                    return False
                
            return True

        # Binary Search for minimum k
        left = 0
        right = len(queries)
        res = len(queries) + 1

        while left <= right:
            mid = (left + right) // 2

            # If zero_array(mid), then move left
            if zero_array(nums, queries[:mid]):
                res = mid
                right = mid - 1

            # If not zero_array(mid), then move right
            else:
                left = mid + 1


        if res > len(queries):
            return -1
        else:
            return res
        

print(Solution().minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
print(Solution().minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))
print(Solution().minZeroArray(nums = [10], queries =[[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]))