from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        

        # Idea: binary search - each mid value is a capability value,
        # with minimum = smallest element in array and maximum = largest element in array

        # For each capability value, loop through the array,
        # rob the house if the value <= capability, else skip the house,
        # and check if the number of robbed houses >= k,
        # if yes then search right, if no then search left

        # Function to check whether you are able to steal from at least k houses,
        # with capability <= value
        def condition(value) -> bool:
            steal_count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= value:
                    steal_count += 1
                    i += 1
                i += 1

            return steal_count >= k


        left, right = 1, max(nums) # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
    
print(Solution().minCapability(nums = [2,3,5,9], k = 2))