from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        # 1. Sort array
        nums.sort()

        # 2. Two pointers (points to min and max),
        # count subsequences that satisfy condition for given min and max
        left, right = 0, len(nums) - 1

        # Record res
        res = 0

        while left <= right:

            # If min + max <= target, add to res, increment left
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1

            # if min + max > target, decrement right
            else:
                right -= 1

        return res % (10 ** 9 + 7)
    
    
print(Solution().numSubseq(nums = [3,5,6,7], target = 9))
print(Solution().numSubseq(nums = [3,3,6,8], target = 10))
print(Solution().numSubseq(nums = [2,3,3,4,6,7], target = 12))