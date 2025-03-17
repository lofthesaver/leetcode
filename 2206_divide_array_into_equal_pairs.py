from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        return all(v % 2 == 0 for v in counts.values())
        
# print(Solution().divideArray(nums = [3,2,3,2,2,2]))
# print(Solution().divideArray(nums =
# [9,9,19,10,9,12,2,12,3,3,11,5,8,4,13,6,2,11,9,19,11,15,9,17,15,12,5,14,12,16,18,16,10,3,8,9,16,20,2,4,16,12,11,14,20,16,2,18,17,20,3,13,16,17,1,1,11,20,20,4]))