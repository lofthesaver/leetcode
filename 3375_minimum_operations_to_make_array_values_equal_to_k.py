from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # Idea: count number of distinct integers greater than k,
        # if k is not the smallest integer than return -1
        distinct_integers = set()
        for v in nums:
            if v < k:
                return -1
            elif v > k:
                distinct_integers.add(v)
                
        return len(distinct_integers)


# print(Solution().minOperations(nums = [5,2,5,4,5], k = 2))
# print(Solution().minOperations(nums = [2,1,2], k = 2))
# print(Solution().minOperations(nums = [9,7,5,3], k = 1))