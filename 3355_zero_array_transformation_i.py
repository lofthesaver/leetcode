from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        # Process all queries in prefix sum manner, 
        # (e.g., prefix_sum[i] indicates the number of times nums[i] is decremented compared to previous),
        # then loop through each number and check if it can be decremented to 0

        prefix_sum = [0] * len(nums)

        for query in queries:
            start, end = query[0], query[1]

            prefix_sum[start] += 1

            if end < len(nums) - 1:
                prefix_sum[end + 1] -= 1

        print(prefix_sum)

        # Process prefix sum
        curr_decrement = 0
        for i in range(len(nums)):
            curr_decrement += prefix_sum[i]

            # If nums[i] cannot be decremented to 0 then return false
            if nums[i] > curr_decrement:
                return False
            
        return True


print(Solution().isZeroArray(nums = [1,0,1], queries = [[0,2]]))
print(Solution().isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
print(Solution().isZeroArray(nums = [1], queries = []))

