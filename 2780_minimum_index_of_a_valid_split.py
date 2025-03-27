from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        # Idea: make prefix sum that stores the number of dominant elements
        # that appears before (including) the number
        # (e.g., prefix_sum[1] stores count of dominant elements before, including nums[1])


        # 1. Find the dominant element
        elements = {}
        for v in nums:
            elements[v] = elements.get(v, 0) + 1

        dominant_element = nums[0]
        max_count = elements[dominant_element]

        for v, count in elements.items():
            if count > max_count:
                dominant_element = v
                max_count = count

        # 2. Create prefix sum array
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = 1 if nums[0] == dominant_element else 0
        
        for i in range(1, len(nums)):
            
            # If nums[i] is the dominant element, then nums[i] = nums[i - 1] + 1,
            # else nums[i] = nums[i - 1]
            if nums[i] == dominant_element:
                prefix_sum[i] = prefix_sum[i - 1] + 1
            else:
                prefix_sum[i] = prefix_sum[i - 1]

        # 3. Loop through the prefix sum array, and try to split at each index i
        for i in range(len(prefix_sum) - 1):

            # If prefix sum is 0, then continue
            if prefix_sum[i] == 0:
                continue

            # Length of left array is i + 1, length of right array is len(nums) - 1 - i
            left_length = i + 1
            right_length = len(prefix_sum) - 1 - i

            # Left array is valid if prefix_sum[i] / left_length > 0.5, 
            # right array is valid if (max_count - prefix_sum[i]) / right_length > 0.5
            if (prefix_sum[i] / left_length) > 0.5 and ((max_count - prefix_sum[i]) / right_length) > 0.5:
                return i

        return -1
        

# print(Solution().minimumIndex(nums = [1,2,2,2]))
# print(Solution().minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1]))
# print(Solution().minimumIndex(nums = [3,3,3,3,7,2,2]))